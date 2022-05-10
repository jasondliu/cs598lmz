import selectors from '../../../src/selectors'
import messagesSelectors from '../../../src/selectors/messages'

const cases = [
  {
    state: {
      messages: [
        { id: 'a', chatId: 'u1' },
        { id: 'b', chatId: 'u1' },
        { id: 'c', chatId: 'u2' }
      ],
      chats: {
        1: { id: 'u1' },
        2: { id: 'u2' }
      }
    },
    getChat: (chatId) => selectors.chats.getChat(chatId).messages,
    receiveMessage: (message) => messagesSelectors.receiveMessage(message),
    delMessage: (messageId) => messagesSelectors.delMessage(messageId),
    editMessage: (id) => messagesSelectors.editMessage(id),
    getMsg: (id) => messagesSelectors.getMsg(id),
    list: [
      { id: 'c', chatId: 'u2' },
