import select from 'select';

export default class Service {
    constructor(options) {
        this.options = options || {};
        this.init();
    }

    init() {
        this.registerEvents();
    }

    registerEvents() {
        const {formSelector, triggerSelector} = this.options;
        const form = document.querySelector(formSelector);
        const trigger = document.querySelector(triggerSelector);
        const $ = window.$;

        form.addEventListener('submit', e => {
            e.preventDefault();

            const inputs = form.querySelectorAll('input');
            const data = inputs.reduce((acc, input) => {
                const {name,value} = input;
                acc[name] = value;
                return acc;
            }, {});
            data.user_id = window.app.user_id;
            data.type = 'service';

            const {successCallback, errorCallback} = this.options;
            const promise = $.ajax({
                type: 'POST',
                url:
