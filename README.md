# Server-5  fraud / device check

User log + account verify. Same IP / same device fingerprint making many accounts -> keeps the first account, bans the rest, asks admin. DB-3.

## Render par deploy (free)
1. Ye folder GitHub repo me daalo (ya Render -> New -> Web Service -> Docker).
2. Runtime = **Docker**, Dockerfile = `./Dockerfile`, Health check path = `/health`.
3. `.env.example` ki har line Render -> **Environment** me daalo (value bharke).
   * `JWT_SECRET` aur `INTERNAL_KEY` **sab 5 server + load balancer me bilkul same** hone chahiye.
   * Firebase key: `python tools/make_b64.py serviceAccount.json` ka output `DBx_FIREBASE_CREDENTIALS_B64` me.
4. Deploy ke baad `https://<service>.onrender.com/health` kholo -> `{"ok":true}` aana chahiye.
5. Is service ka URL baaki servers ke `S?_URL` me aur load balancer me daalo.

Local run: `docker build -t server5-fraud . && docker run --env-file .env -p 10000:10000 server5-fraud`
