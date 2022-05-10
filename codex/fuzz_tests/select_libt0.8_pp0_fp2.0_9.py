import selectNextTab from './selectNextTab';
import listTabs from './listTabs';
import closeTabs from './closeTabs';

const commands = {};
commands.selectTab = selectTab;
commands.selectNextTab = selectNextTab;
commands.listTabs = listTabs;
commands.closeTabs = closeTabs;

/**
 * Call a named command
 *
 * @param {Object} options
 * @param {string} options.name - the command name
 * @param {string[]} options.args - the arguments to pass to the command
 * @returns {Promise}
 */
module.exports = async (options = {}) => {
  const { name, args } = options;
  if (!(name in commands)) {
    throw new Error(`Unknown command: ${name}`);
  }
  commands[name](...args);
};
