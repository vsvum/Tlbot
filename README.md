# 🤖 Telegram Bot — Команды управления

Полезные команды для развёртывания и управления ботом на VPS сервере.

---

## 📦 Установка и первоначальная настройка

```bash
# Обновление системы
apt update && apt upgrade -y

# Установка Python, Git и pip
apt install python3 python3-pip git python3-venv -y

# Клонирование репозитория
cd /root
git clone https://github.com/ВАШ_НИК/ВАШ_РЕПОЗИТОРИЙ.git
cd ВАШ_РЕПОЗИТОРИЙ

# Создание виртуального окружения
python3 -m venv venv

# Активация виртуального окружения
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Создание файла с токеном
nano .env
# Добавьте: BOT_TOKEN=ваш_токен
```

---

## 🚀 Управление сервисом (Systemd)

```bash
# Запуск бота
systemctl start telegram-bot

# Остановка бота
systemctl stop telegram-bot

# Перезапуск бота
systemctl restart telegram-bot

# Проверка статуса
systemctl status telegram-bot

# Включение автозапуска при загрузке
systemctl enable telegram-bot

# Отключение автозапуска
systemctl disable telegram-bot

# Перезагрузка конфигурации сервиса
systemctl daemon-reload
```

---

## 📊 Мониторинг и логи

```bash
# Просмотр логов в реальном времени
journalctl -u telegram-bot -f

# Последние 50 строк логов
journalctl -u telegram-bot -n 50 --no-pager

# Логи за сегодня
journalctl -u telegram-bot --since today

# Использование ресурсов (CPU, RAM)
systemctl status telegram-bot

# Проверка процесса
ps aux | grep python

# Проверка порта (если бот использует вебхуки)
netstat -tulpn | grep python
```

---

## 🔄 Обновление бота

```bash
# Переход в папку бота
cd /root/ВАШ_РЕПОЗИТОРИЙ

# Активация виртуального окружения
source venv/bin/activate

# Получение обновлений из GitHub
git pull

# Обновление зависимостей (если изменился requirements.txt)
pip install -r requirements.txt

# Перезапуск бота
systemctl restart telegram-bot
```

---

## 🛠️ Отладка и диагностика

```bash
# Запуск бота вручную (для отладки)
cd /root/ВАШ_РЕПОЗИТОРИЙ
source venv/bin/activate
python bot.py

# Проверка файла .env
cat .env

# Проверка установленных пакетов
pip list

# Проверка версии Python
python --version

# Проверка доступного места на диске
df -h

# Проверка загруженности памяти
free -h
```

---

## 🔐 Безопасность

```bash
# Смена пароля root
passwd

# Настройка фаервола
apt install ufw -y
ufw allow ssh
ufw enable
ufw status

# Проверка активных подключений SSH
who

# Просмотр последних входов в систему
last

# Блокировка подозрительных IP (пример)
ufw deny from 192.168.1.1
```

---

## 🧹 Очистка и обслуживание

```bash
# Очистка кэша pip
pip cache purge

# Очистка кэша apt
apt clean
apt autoclean

# Удаление ненужных пакетов
apt autoremove -y

# Поиск больших файлов
du -ah /root | sort -rh | head -20

# Очистка старых логов
journalctl --vacuum-time=7d
```

---

## 📋 Быстрая шпаргалка

| Действие | Команда |
|----------|---------|
| **Статус бота** | `systemctl status telegram-bot` |
| **Перезапуск** | `systemctl restart telegram-bot` |
| **Логи** | `journalctl -u telegram-bot -f` |
| **Обновить** | `git pull && systemctl restart telegram-bot` |
| **Остановить** | `systemctl stop telegram-bot` |

---

## ⚠️ Важные заметки

1. **Виртуальное окружение:** Всегда активируйте перед работой с Python:
   ```bash
   source venv/bin/activate
   ```

2. **Токен бота:** Никогда не коммитьте файл `.env` в Git! Добавьте его в `.gitignore`:
   ```bash
   echo ".env" >> .gitignore
   ```

3. **Резервное копирование:** Перед крупными изменениями сделайте бэкап:
   ```bash
   cp -r /root/ВАШ_РЕПОЗИТОРИЙ /root/ВАШ_РЕПОЗИТОРИЙ_backup
   ```

4. **Время сервера:** Проверьте часовой пояс:
   ```bash
   timedatectl
   # Установка MSK времени
   timedatectl set-timezone Europe/Moscow
   ```

---

## 🆘 Если что-то пошло не так

```bash
# Полная перезагрузка сервера
reboot

# Проверка всех сервисов
systemctl --failed

# Пересоздание сервиса (если файл повреждён)
rm /etc/systemd/system/telegram-bot.service
# Затем создайте заново через nano
```

---

