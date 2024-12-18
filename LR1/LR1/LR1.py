#LR1
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# Заменить токен
vk_session = vk_api.VkApi(token='your_token')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# Создаем клавиатуру с кнопками
keyboard = {
    "one_time": False,
    "buttons": [
        [
            {
                "action": {
                    "type": "text",
                    "label": "Привет",
                    "payload": "{\"button\": \"hello\"}"
                },
                "color": "positive"
            }
        ],
        [
            {
                "action": {
                    "type": "text",
                    "label": "Пока",
                    "payload": "{\"button\": \"bye\"}"
                },
                "color": "negative"
            }
        ]
    ]
}

# Преобразуем клавиатуру в JSON строку
keyboard = vk_api.keyboard.VkKeyboard.get_keyboard(keyboard)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        user_id = event.user_id

        if user_message == 'привет' or user_message == 'привет':
            vk.messages.send(user_id=user_id, message='Привет!', random_id=0, keyboard=keyboard)
        elif user_message == 'пока' or user_message == 'пока':
            vk.messages.send(user_id=user_id, message='Пока!', random_id=0, keyboard=keyboard)
        else:
            vk.messages.send(user_id=user_id, message='Не понимаю тебя :(', random_id=0, keyboard=keyboard)