import selectors from 'modules/shared/entity/entitySelectors';
import destroyActions from 'modules/auth/auth/destroy/authDestroyActions';
import destroySelectors from 'modules/auth/auth/destroy/authDestroySelectors';
import actions from 'modules/auth/auth/list/authListActions';
import paginationSelectors from 'modules/shared/pagination/paginationSelectors';
import selectors from 'modules/auth/auth/list/authListSelectors';
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';
import TableWrapper from 'view/shared/styles/TableWrapper';
import ButtonLink from 'view/shared/styles/ButtonLink';
import FilesListView from 'view/shared/list/FileListView';
import UserListItem from 'view/iam/list/UserListItem';
import CustomerListItem from 'view/customer/list/CustomerListItem';
import RentListItem from 'view/rent/list/RentListItem';
import Booking
