import selector from '../store/selectors'
import * as actions from '../store/actions'
import * as Sentry from '@sentry/browser'
import { get } from 'lodash'
import {
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  FormControl,
  InputLabel,
  Input,
  InputAdornment,
  IconButton,
  TextField,
  DialogActions,
  Tooltip,
  LinearProgress,
  Typography,
  FormHelperText,
  DialogContentText
} from '@material-ui/core'
import { VisibilityOff, Visibility } from '@material-ui/icons'
import { connect } from 'react-redux'
import { withStyles } from '@material-ui/core/styles'

const styles = theme => ({
  button: {
    margin: theme.spacing.unit
  },
  textField: {
    marginLeft: theme.spacing.unit,
    marginRight: theme.spacing.unit
  },
  progress
