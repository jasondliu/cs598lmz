import _struct from '../lib/struct'
import { action } from 'mobx'

export default class BackboneMaoStore {
    constructor(model, options = {}) {
        let {setters = {}, getters = {}} = options;
        this.model = model;
        this.getters = getters;
        this.setters = setters;
        if (model.isValid()) {
            _struct.handler(this);
        }
    }

    @action
    modelSet(model, options) {
        let {setters = {}} = this;
        model.each((attr, v) => {
            if (_.has(setters, attr)) {
                (setters[attr])(model, v, options);
            }
        });
    }

    @action
    modelGet(model, options) {
        let {getters = {}} = this;
        model.each((attr, v) => {
            if (_.has(getters, attr)) {
                (getters[attr])(model, v, options);
            }
