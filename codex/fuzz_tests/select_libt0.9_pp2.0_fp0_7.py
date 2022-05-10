import selector from './depth.selector';
import { swapPosition } from '../position/position.actions';
import { socket, socketId } from '../socket/socket.reducer';

const initialState = {
  0: {
    price: 100,
    size: 1000,
    count: 1,
  },
  1: {
    price: 99,
    size: 1000,
    count: 1,
  },
  2: {
    price: 98,
    size: 1000,
    count: 1,
  },
  3: {
    price: 97,
    size: 1000,
    count: 1,
  },
  4: {
    price: 96,
    size: 1000,
    count: 1,
  },
};

describe('depth reducer', () => {
  describe('selector', () => {
    it('should exist', () => {
      expect(selector).to.exist;
    });

    it('should select the deep object', () => {
      expect(selector({ depth: initialState })).to.deep
