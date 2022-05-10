import select from '@tinkoff/utils/array/select';
import forEach from '@tinkoff/utils/array/forEach';
import find from '@tinkoff/utils/array/find';
import findIndex from '@tinkoff/utils/array/findIndex';
import some from '@tinkoff/utils/array/some';
import propEq from '@tinkoff/utils/object/propEq';
import getOr from '@tinkoff/utils/object/getOr';
import filtration from '@tinkoff/utils/array/filtration';
import set from '@tinkoff/utils/object/set';

const SET_FILTER_VALUE = 'SET_FILTER_VALUE';
const GET_FILTER_VALUE = 'GET_FILTER_VALUE';
const SET_FILTER_VALUE_BACK = 'SET_FILTER_VALUE_BACK';
const FILTER_CATEGORY = 'FILTER_CATEGORY';
const FILTER_PROPERTIES = 'FILTER_PROPERTIES';
const FILTER_PRICE
