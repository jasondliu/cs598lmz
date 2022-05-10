import select from '_select'
import { Container } from '_shared'
import { getIn } from 'immutable'

import { takeLatest } from '@helpers/saga'

import { logoutSaga } from '_features/user/auth'

import {
  signOut,
  setIsAuth,
  setError,
  setIsPhoneAuth
} from './reducer'

import {
  LOGOUT_REQUEST,
  LOGOUT_CANCEL
} from './actions'

import {
  getAuthState as getAuthStateFromFirebase,
  signOut as signOutFromFirebase
} from '_firebase'

import { getUserDataFromModel } from '_features/user/model'

function* authCheck() {
  const isAuth = yield select(select.auth.isAuth)

  if (!isAuth) {
    yield takeLatest(getAuthStateFromFirebase(), authListener);
  }
}

function* authListener(auth) {
  const isSigned = getIn(auth, ['signed', 'is
