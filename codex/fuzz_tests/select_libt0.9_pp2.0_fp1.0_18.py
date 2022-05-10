import selectStores from '../utils/selectors';
import getSimpleMode from '../utils/getSimpleMode';

import { debug } from '../../../utils/log';
import { errorBoundary } from '../../../utils/errorBoundary';

import ContentBox from '../../atoms/contentBox/index';
import SlideFrame from '../../organisms/slideFrame/index';
import RevealBar from '../../molecules/revealBar/index';
import Loader from '../../atoms/loader';

import {
  getContentData,
  getDataFromServer,
  resetReduxStore
} from '../actions';

import contentTypes from '../utils/contentTypes';

import {
  getContent,
  getCurrentContent,
  getIsFetchingData,
  getContentType
} from '../selectors';


const getIsSmallestMediaQuery = mediaQuery.getIsSmallestMediaQuery;
const debounce = _.debounce;

// Prepare child components
const SlideFrameWithRedux = connect(selectStores(
  get
