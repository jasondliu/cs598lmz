import selector from './selector';

/**
 * Component
 */
const Component = ({
  className,
  isHome,
  isLoggedIn,
  isLoading,
  loggedInUser,
  onLogIn,
  onLogOut,
  onSignUp,
  onToggleMenu,
  showMenu,
  toggleMenuButtonProps,
}) => {
  const classes = classnames(styles.root, className);

  const [isMenuVisible, setIsMenuVisible] = useState(false);

  const handleToggleMenu = useCallback(() => {
    setIsMenuVisible(!isMenuVisible);
  }, [isMenuVisible]);

  useEffect(() => {
    setIsMenuVisible(false);
  }, [isHome]);

  return (
    <div className={classes}>
      <div className={styles.brand}>
        <Link href="/">
          <a className={styles.link}>
            <img
              className={styles.image}
              src="/images/logo-white
