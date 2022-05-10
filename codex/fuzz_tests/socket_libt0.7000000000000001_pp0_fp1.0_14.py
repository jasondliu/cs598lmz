import socket from 'socket.io-client';
import {
  FETCH_SINGLE_MESSAGE_REQUEST,
  FETCH_SINGLE_MESSAGE_SUCCESS,
  FETCH_SINGLE_MESSAGE_FAILURE,
  SEND_NEW_MESSAGE,
  SEND_NEW_MESSAGE_SUCCESS,
  SEND_NEW_MESSAGE_FAILURE,
  FETCH_MESSAGES_REQUEST,
  FETCH_MESSAGES_SUCCESS,
  FETCH_MESSAGES_FAILURE
} from '../constants';

const io = socket();

const fetchSingleMessage = (payload) => ({
  type: FETCH_SINGLE_MESSAGE_REQUEST,
  payload
});

const fetchSingleMessageSuccess = (payload) => ({
  type: FETCH_SINGLE_MESSAGE_SUCCESS,
  payload
});

const fetchSingleMessageFailure =
