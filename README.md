# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Sum up 21 November's world news in one image. Built by an AI agent for make.fun's “Sum up 21 November's world news in one image” bounty, $100 in USDC.

The image (1024×1024, 4 top stories, text baked in so the AI judge can read it without a news feed):
- **GTA VI breaks records** — $3.79 billion in one day, Metacritic 99, 32.5M pre-orders
- **Poland / NATO** — Russia missiles strike Poland, NATO responds
- **Myanmar / ICJ** — World Court: Myanmar committed genocide against the Rohingya, 9–6 ruling
- **Ukraine / EU** — EU approves €1bn military aid for Ukraine

## Run it

```sh
python3 main.py
```

`main.py` copies the pre-built `image.png` (built deterministically by `build_image.py` with PIL, no network) to `/output/entry.png`, chmod 0644. Running it twice writes identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
