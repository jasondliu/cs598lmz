import select from 'select'
import Event from './event'
import getUid from './get-uid'
import './dragdrop.css'

export default class DragDrop {
  /**
   * @param {HTMLElement} el - The container element
   * @param {Object} [options]
   * @param {String} [options.groupName]
   * @param {Number} [options.maxNumberOfFiles]
   * @param {Number} [options.maxFileSize]
   * @param {Number} [options.maxTotalFileSize]
   * @param {Array} [options.acceptedFileTypes]
   * @param {Function} [options.beforeDrop]
   * @param {Function} [options.onDrop]
   * @param {Function} [options.onDragEnter]
   * @param {Function} [options.onDragLeave]
   * @param {Function} [options.beforeUpload]
   * @param {Function} [options.onUpload]
   */
  constructor (el, options) {
    if (typeof el ===
