# IDX Multi-Agent Real Estate Assistant

IDX Exchange AI Agentic Engineer Internship, Summer 2026.

A multi-agent AI assistant built on [OpenClaw](https://github.com/openclaw/openclaw) that answers real estate questions over two MLS datasets:

| Table | Contents |
|---|---|
| `rets_property` | Active California MLS listings (130+ fields) |
| `california_sold` | Sold and closed transactions, 2021–2025 (46 fields) |

**LLM provider:** Google Gemini (`gemini-2.5-flash` for generation, `gemini-embedding-001` for embeddings). Gemini replaces the OpenAI examples in the handbook, as approved by the team lead.

## Progress

| Week | Module | Status |
|---|---|---|
| 0 | Environment setup | 🟡 In progress |
| 1 | OpenClaw architecture | 🟡 In progress (see [docs/architecture.md](docs/architecture.md)) |
| 2 | Natural-language property search | ⬜ |
| 3 | MLS database integration | ⬜ |
| 4 | Conversational agent | ⬜ |
| 5 | Market analytics | ⬜ |
| 6 | Embeddings and vector search | ⬜ |
| 7 | Recommendation engine | ⬜ |
| 8 | RAG pipeline | ⬜ |
| 9 | Multi-agent orchestration | ⬜ |
| 10 | WhatsApp layer | ⬜ |
| 11 | Email agents and safety | ⬜ |
| 12 | Capstone demo | ⬜ |

## Setup

```bash
# 1. Python env
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2. Secrets
cp .env.example .env   # then fill in values

# 3. Import the MLS dumps (place them in data/; they are git-ignored)
mysql -u root -p -e "CREATE DATABASE idx_exchange CHARACTER SET utf8mb4;"
mysql -u root -p idx_exchange < data/rets_property.sql
mysql -u root -p idx_exchange < data/california_sold.sql

# 4. Verify everything
python scripts/verify_setup.py
```

## Repo layout

```
docs/      architecture notes and diagrams
scripts/   setup and utility scripts
sql/       reusable SQL (sanity checks, analytics)
data/      local MLS dumps (git-ignored, confidential)
```

## Data handling

MLS data is confidential. SQL dumps, `.env`, and generated embeddings are never committed.
