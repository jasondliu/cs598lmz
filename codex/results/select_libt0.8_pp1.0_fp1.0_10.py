import selectn from 'selectn'
import { stringify } from 'query-string'
import jsonify from '../utils/jsonify'
import { notify } from 'react-notify-toast'

const { logout } = require('../utils/auth')

export const updateAvatar = (user, file) => {
  const { currentUser } = user
  const uid = selectn('uid', currentUser)

  return (dispatch) => {
    dispatch(statusRequest())

    return wrapFile(file).then(({ data, filename }) => {
      const dataUrl = 'data:' + data.contentType + ';base64,' + data.data
      return db
        .storage()
        .child(`avatars/${filename}`)
        .putString(dataUrl, 'data_url')
        .then((snap) => {
          return db
            .storage()
            .child(`avatars/${filename}`)
            .getDownloadURL()
            .then((url) => {
              return db
                .collection('users')
                .doc
