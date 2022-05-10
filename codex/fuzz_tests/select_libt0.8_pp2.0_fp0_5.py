import selection from './selection';
import createFile from './createFile';
import editor from './editor';
import autocomplete from './autocomplete';
import code from './code';
import hint from './hint';
import git from './git';
import keymap from './keymap';
import settings from './settings';
import modal from './modal';
import token from './token';
import settingsPage from './settingsPage';
import publishModal from './publishModal';
import publish from './publish';
import connection from './connection';
import statusBar from './statusBar';

export default combineReducers({
  auth: auth,
  user: user,
  file: file,
  selection: selection,
  createFile: createFile,
  editor: editor,
  autocomplete: autocomplete,
  code: code,
  hint: hint,
  git: git,
  keymap: keymap,
  settings: settings,
  modal: modal,
  token: token,
  settingsPage: settings
