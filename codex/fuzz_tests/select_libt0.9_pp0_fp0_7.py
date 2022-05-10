import selectTemplate from './select.html';
import { angular } from 'entcore';

export class SelectController {
    ngModel;
    selected;
    placeholder;
    items = [];
    functionToExecute = item => item.id;
    constructor(){}
    $onInit () {
        if (this.ngModel) {
            this.ngModel = this.functionToExecute(this.ngModel);
        }
        this.updateContext();
    }
    updateContext () {
        this.selected = this.items.filter(element => {
            return element.id === this.ngModel;
        })[0];
    }
    changeContext () {
        this.ngModel = this.functionToExecute(this.selected);
    }
}

export const select = angular.module('select', [])
    .component('select', {
        template: selectTemplate,
        controller: SelectController,
        transclude: true,
        bindings: {
            ngModel: '=',
            placeholder: '<',
            items: '=',
            functionTo
