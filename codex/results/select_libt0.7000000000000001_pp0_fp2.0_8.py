import select from 'select';

class Component extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      isOpen: false
    };
  }

  componentDidMount() {
    const {
      isOpen
    } = this.state;

    if (isOpen) {
      this.enableBodyScroll();
    }
  }

  componentDidUpdate(prevProps, prevState) {
    const {
      isOpen
    } = this.state;
    const {
      isOpen: wasOpen
    } = prevState;

    if (isOpen === wasOpen) {
      return;
    }

    if (isOpen) {
      this.enableBodyScroll();
    } else {
      this.disableBodyScroll();
    }
  }

  componentWillUnmount() {
    const {
      isOpen
    } = this.state;

    if (isOpen) {
      this.disableBodyScroll();
    }
  }

  enableBodyScroll() {
    const {overlayEl} =
