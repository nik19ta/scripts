package main

import (
	"log"

	tgbotapi "github.com/Syfaro/telegram-bot-api"
)

// это бот который отвечает на ваше сообщение в телеграмме
func main() {
	bot, err := tgbotapi.NewBotAPI("TOKEN")
	if err != nil {
		log.Panic(err)
	}

	bot.Debug = false
	log.Printf("Authorized on account %s", bot.Self.UserName)

	var ucfg tgbotapi.UpdateConfig = tgbotapi.NewUpdate(0)
	ucfg.Timeout = 60
	upd, _ := bot.GetUpdatesChan(ucfg)
	// читаем обновления из канала
	for {
		select {
		case update := <-upd:
			// Пользователь, который написал боту
			UserName := update.Message.From.UserName
			// id чата на который посылаем что либо
			ChatID := update.Message.Chat.ID
			// Текст сообщения
			Text := update.Message.Text

			var reply string = UserName + ", вы прислали: " + Text

			send(ChatID, bot, reply)
		}

	}
}

func send(ChatID int64, bot *tgbotapi.BotAPI, text string) {
	msg := tgbotapi.NewMessage(ChatID, text)
	bot.Send(msg)
}
