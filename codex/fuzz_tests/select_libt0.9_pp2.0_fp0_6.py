import select from 'select';
import DefaultClient from './DefaultClient';

const defaultInstance = new DefaultClient();

const globalAgent = new Agent({ keepAlive: true });
globalAgent.setMaxListeners(0);
globalAgent.createConnection = createConnection;

function checkMaxContentLength(client, response) {
  const maxContentLength = client.defaults.headers['Content-Length']
    ? parseInt(client.defaults.headers['Content-Length'], 10)
    : undefined;

  if (maxContentLength && response.contentLength > maxContentLength) {
    throw new Error(
      `Content Length: ${maxContentLength} larger than max ${maxContentLength}, client options may be needed`
    );
  }
}

function createConnection(opts, callback) {
  opts.createConnection = select(opts);
  opts.defaultPort = opts.defaultPort || 80;
  opts.port = opts.port || 80;
  opts.host = opts.hostname || opts.host || 'localhost';
  (opts as
