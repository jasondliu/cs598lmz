import select2 from 'select2';

var Repository = require('../repository.js');

var Step1 = React.createClass({
    /**
     * Converts form into json
     * @returns {*}
     */
    formToObject: function(selector) {
        var form = $(selector);
        var objects = form.serializeArray();
        var result = {};

        _.each(objects, function(item){
            result[item.name] = item.value;
        });

        return result;
    },

    getInitialState: function() {
        return {
            changeType: null,
            item: {
                id: null,
                type: "",
                title: "",
                description: "",
                list: null,
                backlog: null,
                status: null,
                log: null,
                points_allocated: null,
                points_spent: null,
                items: null,
            },
            lists: [
                {id: 1, name: "First list"},
                {id: 2, name
