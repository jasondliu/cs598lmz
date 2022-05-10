import select from 'select';
import 'select2/dist/css/select2.min.css';
import 'select2';
import $ from 'jquery';
import 'jquery-ui/ui/widgets/sortable';
import { debounce } from 'lodash';

$(document).on('select2:select select2:unselect', function (e) {
    const select = e.currentTarget;
    const type = e.type;
    const sortableList = select.getAttribute('data-sortable');
    const options = select.querySelectorAll('option');
    const selectedOptions = select.querySelectorAll('option:checked');

    if (sortableList) {
        const sortable = document.getElementById(sortableList);
        const selectedValues = [...selectedOptions].map(option => option.getAttribute('value'));

        sortable.innerHTML = '';

        [...options]
            .filter(option => selectedValues.includes(option.getAttribute('value')))
            .forEach(option => {
                const li = document.createElement
