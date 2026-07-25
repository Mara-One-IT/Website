import anthropic

client = anthropic.Anthropic()

SESSION_ID = "sesn_015nK5qcspgcfefMCEk98ZLw"

# List all output files from the session
files = client.beta.files.list(
    scope_id=SESSION_ID,
    betas=["managed-agents-2026-04-01"],  # required alongside the auto-added files beta
)

# Download each file
import os
for f in files:
    os.makedirs(os.path.dirname(f.filename) if os.path.dirname(f.filename) else ".", exist_ok=True)
    resp = client.beta.files.download(f.id)
    with open(f.filename, "wb") as out:
        out.write(resp.read())
    print(f"Downloaded: {f.filename} ({f.size_bytes} bytes)")
