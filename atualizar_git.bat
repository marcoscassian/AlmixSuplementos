@echo off
cd C:\UsersDocuments\AlmixSuplementos
git rm -r --cached env
git commit -m "Remove env do repositório"
git push origin main
git add .
git commit -m "Atualizado automaticamente"
git push origin main
pause