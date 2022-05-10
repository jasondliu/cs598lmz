import selectize from 'selectize';

import { Meteor } from 'meteor/meteor';
import { Bert } from 'meteor/themeteorchef:bert';
import { upsertRole, removeRole } from '../../../api/roles/methods.js';

const handleUpsert = () => {
  const { role } = Session.get('selectedRole');
  const confirmation = role && role._id ? 'Role updated!' : 'Role added!';
  const upsert = {
    name: document.querySelector('[name="name"]').value.trim(),
    description: document.querySelector('[name="description"]').value.trim(),
  };

  if (role && role._id) upsert._id = role._id;

  upsertRole.call(upsert, (error, response) => {
    if (error) {
      Bert.alert(error.reason, 'danger');
    } else {
      document.querySelector('[name="name"]').value = '';
      document.querySelector('[name="description"]').
