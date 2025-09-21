@echo off
cd C:\UsersDocuments\AlmixSuplementos
git rm -r --cached __pycache__
git rm -r --cached env
git commit -m "Remove arquivos ignorados"
git push origin main
git add .
git commit -m "Atualizado automaticamente"
git push origin main
pause