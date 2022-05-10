import select from 'select'
import { fork } from 'child_process'
import utils from './utils'
import * as path from 'path'

const websocket = () => {
  const app = http.createServer(serverHandler)
  const io: SocketIO.Server = socketIo(app)
  process.on('SIGINT', () => {
    console.log('process exit')
    process.exit()
  })
  process.on('uncaughtException', () => {
    console.log('process exception')
    process.exit()
  })
  process.on('exit', () => {
    console.log('process exit')
  })
  io.on('connect', (socket: Socket) => {
    console.log('Connected client on port %s.', port)
    let paths = []
    const time = utils.formatDate(new Date(), 'yyyy-MM-dd hh:mm:ss')
    console.log(`${time} connected to ${socket.request.connection.remoteAddress.split(':')[3]}`)
   
