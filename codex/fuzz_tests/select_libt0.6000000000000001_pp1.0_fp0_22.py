import selectors from './selectors';

const { getRemainingTime } = selectors;

describe('remainingTime selector', () => {
    it('should return remaining time in seconds', () => {
        const state = {
            timerStatus: TIMER_STATUS.RUNNING,
            time: {
                startTime: moment().subtract(4, 'minutes'),
                duration: moment.duration(5, 'minutes')
            }
        };

        expect(getRemainingTime(state)).toEqual(60);
    });

    it('should return 0 if there is no remaining time', () => {
        const state = {
            timerStatus: TIMER_STATUS.RUNNING,
            time: {
                startTime: moment(),
                duration: moment.duration(5, 'minutes')
            }
        };

        expect(getRemainingTime(state)).toEqual(0);
    });

    it('should return 0 if timer is not running', () => {
        const state = {
            timerStatus: TIMER_STATUS.STOP
