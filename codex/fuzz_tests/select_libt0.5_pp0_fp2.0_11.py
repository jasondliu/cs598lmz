import selectors from 'modules/shared/importer/importerSelectors';
import actions from 'modules/shared/importer/importerActions';
import fields from 'modules/auth/user/importer/userImporterFields';
import { i18n } from 'i18n';

class UserImportPage extends Component {
  state = {
    saving: false,
  };

  doSubmit = async (_, data) => {
    try {
      this.setState({
        saving: true,
      });

      await dispatch(
        actions.doImport(data),
      );

      Message.success(
        i18n('entities.auth.importer.fileName.success'),
      );

      getHistory().push('/auth/user');
    } catch (error) {
      Errors.handle(error);

      this.setState({
        saving: false,
      });
    }
  };

  render() {
    const { saving } = this.state;

    return (
      <ToolbarWrapper>
        <ToolbarItem
          wrapperClassName="
