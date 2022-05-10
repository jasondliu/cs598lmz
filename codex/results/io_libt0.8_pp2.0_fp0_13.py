import io.reactivex.Single
import org.koin.dsl.module
import java.util.concurrent.TimeUnit

class MainFragment : Fragment() {
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val viewModel: MainViewModel = getViewModel()
        val binding = MainFragmentBinding.inflate(inflater, container, false)
        binding.lifecycleOwner = viewLifecycleOwner
        binding.viewModel = viewModel

        return binding.root
    }

    companion object {
        fun newInstance() = MainFragment()
    }
}

class MainViewModel : ViewModel() {
    val name: ObservableField<String> = ObservableField("")
    val onClick: Single<String> = Single.timer(1, TimeUnit.SECONDS)
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
        .map {
