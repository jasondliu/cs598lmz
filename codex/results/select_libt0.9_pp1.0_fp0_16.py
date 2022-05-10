import selectTicket from './selectTicket';
import session from 'express-session';
import webpack from 'webpack';
import webpackDevServer from 'webpack-dev-server';
import webpackMiddleware from 'webpack-dev-middleware';
import setLanguage from './setLanguage';
// import parser from 'body-parser';

const browserSync = require('browser-sync').create();
const env = process.env.NODE_ENV || 'development';
const isProduction = env === 'production';
const isDeveloping = env === 'development';

/**
 * Configure Node.js app
 */
/* eslint no-console: 0 */

// Set default node environment to development
process.env.NODE_ENV = process.env.NODE_ENV || 'development';

// Register babel to have ES6 support on the server
require('babel-register');

// Express configuration
const app = express();
app.set('trust proxy', true);
app.use(logger('dev'));
app.use(bodyParser.json());
app.use
