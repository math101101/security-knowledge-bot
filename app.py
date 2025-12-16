import json
import sys
from dataclasses import dataclass
from typing import List, Dict, Any, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class KBItem:
    id: str
    title: str
    tags: List[str]
    content: str
    source: str


def load_kb(path: str) -> List[KBItem]:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    items = []
    for it in raw.get("items", []):
        items.append(
            KBItem(
                id=str(it.get("id", "")),
                title=str(it.get("title", "")),
                tags=list(it.get("tags", [])),
                content=str(it.get("content", "")),
                source=str(it.get("source", "")),
            )
        )
    if not items:
        raise ValueError("Base de conhecimento vazia. Adicione itens em kb.json")
    return items


def build_corpus(items: List[KBItem]) -> List[str]:
    corpus = []
    for it in items:
        text = f"{it.title}\nTags: {' '.join(it.tags)}\n{it.content}\nFonte: {it.source}"
        corpus.append(text)
    return corpus


class SecurityKnowledgeBot:
    def __init__(self, items: List[KBItem]):
        self.items = items
        self.corpus = build_corpus(items)

        # TF-IDF simples, bom o suficiente e leve
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words=None,      # PT-BR varia muito; melhor não forçar stopwords aqui
            ngram_range=(1, 2),
            max_features=12000
        )
        self.tfidf = self.vectorizer.fit_transform(self.corpus)

    def search(self, query: str, top_k: int = 3) -> List[Tuple[KBItem, float]]:
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.tfidf).flatten()

        ranked_idx = sims.argsort()[::-1][:top_k]
        results = []
        for idx in ranked_idx:
            score = float(sims[idx])
            if score <= 0.0:
                continue
            results.append((self.items[idx], score))
        return results

    def answer(self, query: str) -> str:
        results = self.search(query, top_k=3)

        if not results:
            return (
                "Não encontrei algo direto na base ainda.\n"
                "Tenta perguntar usando termos como: OWASP, ISO 27001, XSS, SQLi, MFA, GDPR.\n"
                "Ou adicione um novo item no kb.json 😄"
            )

        # Melhor match
        best_item, best_score = results[0]

        # Resposta curta + referências
        lines = []
        lines.append(f"📌 {best_item.title}")
        lines.append(best_item.content.strip())
        lines.append("")
        lines.append(f"🔎 Fonte: {best_item.source} | ID: {best_item.id} | Relevância: {best_score:.2f}")

        # Sugestões relacionadas
        if len(results) > 1:
            lines.append("")
            lines.append("➡️ Relacionados:")
            for it, sc in results[1:]:
                lines.append(f"- {it.title} (ID: {it.id}, {sc:.2f})")

        return "\n".join(lines)


def main():
    kb_path = "kb.json"
    if len(sys.argv) > 1:
        kb_path = sys.argv[1]

    items = load_kb(kb_path)
    bot = SecurityKnowledgeBot(items)

    print("Security Knowledge Bot (local) 🔐")
    print("Digite sua pergunta (ou 'sair')\n")

    while True:
        try:
            q = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando.")
            break

        if not q:
            continue
        if q.lower() in {"sair", "exit", "quit"}:
            print("Até mais!")
            break

        print("\nBot:\n" + bot.answer(q) + "\n")


if __name__ == "__main__":
    main()
