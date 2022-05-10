import select from 'select';
import {
  setUser,
  setError,
  setRepos,
  setOrg,
  setOrgs,
  setLoading
} from 'actions/user-actions';

// I really think this should be in a config file somewhere.
const githubUrl = 'https://api.github.com';

/**
 * Retrieve a user's repos and organizations.
 * @param {Object} user - The user object.
 * @returns {Promise}
 */
export function getUserInfo(user) {
  const { username } = user;

  return function (dispatch) {
    dispatch(setLoading(true));

    // Get user repos.
    let repoPromise = fetch(`${githubUrl}/users/${username}/repos`)
      .then(response => response.json())
      .then(repos => dispatch(setRepos(repos)));

    // Get orgs that the user is a member of.
    let orgPromise = fetch(`${githubUrl}/users/${username}/orgs`)

