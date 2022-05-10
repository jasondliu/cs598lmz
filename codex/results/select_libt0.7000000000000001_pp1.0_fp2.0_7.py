import selectn from 'selectn';
import flatten from 'lodash/flatten';
import {isEqual} from 'lodash';
import {createSelector} from 'reselect';
import {getEntity} from './entities';
import {getUserId} from './users';
import {getShares, getStorages, getStorageById} from './storages';

const getFiles = state => selectn('files.items', state) || {};
const getFolders = state => selectn('folders.items', state) || {};

const getFolderById = (state, {folderId}) => {
  const folders = getFolders(state);
  const folder = folders[folderId];

  if (!folder) {
    return null;
  }

  return folder;
};

const getFileById = (state, {fileId}) => {
  const files = getFiles(state);
  const file = files[fileId];

  if (!file) {
    return null;
  }

  return file;
};

const getFolder
