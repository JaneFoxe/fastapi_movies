Приложение для создания списка фильмов, которые планируете посмотреть, чтобы они лежали в одном месте и не потерялись. 


Создание репозитория

git init
git remote add origin git@github.com:<никнейм>/<названиеРепозитория>.git
.... add gitignore
git add .
git commit -m "..."
git branch -M main
git push -u origin main

Подготовка сервера

sudo apt-get update
sudo apt-get install git

Докер

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

Запуск приложения

1. Создание образа с приложением
   
docker build . --tag fastapi_app

2.Запуск образа в контейнере с пробросом портов для доступа к контейнеру из интернета

docker run -p 80:80 fastapi_app

