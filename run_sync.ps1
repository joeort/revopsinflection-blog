$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

python sync.py
if ($LASTEXITCODE -ne 0) {
    Write-Error "sync.py failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
}

git add -A
$diff = git diff --cached --quiet; $hasChanges = ($LASTEXITCODE -ne 0)
if ($hasChanges) {
    git commit -m "chore: sync latest Substack posts"
    git push
} else {
    Write-Output "No changes to commit"
}
