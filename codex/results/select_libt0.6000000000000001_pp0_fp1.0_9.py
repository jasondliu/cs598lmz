import select from '../select'

export default function* onReset() {
  while (true) {
    yield take(constants.RESET)
    yield put(actions.reset())
    yield call(reset, select)
  }
}
