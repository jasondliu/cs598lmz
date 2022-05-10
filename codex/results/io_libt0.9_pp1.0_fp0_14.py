import io.github.sainak.trackmysleepquality.sleepquality.SleepQualityViewModelFactory
import io.github.sainak.trackmysleepquality.sleeptracker.SleepTrackerViewModelFactory

class InjectorUtils {

    companion object {

        private fun getSleepDatabase(context: Context): SleepDatabaseDao {
            return SleepDatabase.getInstance(context.applicationContext).sleepDatabaseDao
        }

        fun provideSleepTrackerViewModelFactory(
            fragment: SleepTrackerFragment
        ): SleepTrackerViewModelFactory {
            val sleeptDatabaseDao = getSleepDatabase(fragment.requireContext())
            return SleepTrackerViewModelFactory(sleeptDatabaseDao, fragment)
        }

        fun provideSleepQualityViewModelFactory(
            fragment: SleepQualityFragment
        ): SleepQualityViewModelFactory {
            val sleepQualityDao = getSleepDatabase(fragment.requireContext())
            return SleepQualityViewModelFactory(sleepQualityDao, fragment.arguments!!.getLong(fragment.KEY_NIGHT_ID))
        }

        fun provideSleepDetail
