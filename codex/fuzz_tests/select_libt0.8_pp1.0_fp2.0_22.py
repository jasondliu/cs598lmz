import select from '../select'
import schema from '../util/schema'

export default component =>
  component.extend({
    props: {
      isBusy: { type: Boolean, default: false },
      items: Array,
      options: Array,
      searchable: { type: Boolean, default: false },
      selected: { default: () => [] },
      vertical: { type: Boolean, default: false }
    },

    data () {
      return {
        activated: false,
        filtered: [],
        filteredOptions: [],
        internalValue: this.selected
      }
    },

    mounted () {
      if (!schema.validate(this.internalValue)) {
        warn(
          'Selected items must be an array of strings or an array of objects.'
        )
      }

      this.filtered = this.internalValue
      this.filteredOptions = this.options
      this.selected = this.internalValue
    },

    methods: {
      /**
       * Return options with `checked` property.
       *
       * @return
