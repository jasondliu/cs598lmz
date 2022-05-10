import io.fabric8.kubernetes.api.model.VolumeMount;

/**
 * @author <a href="mailto:michaelschuetz83@gmail.com">Michael Schuetz</a>
 */
public class KubernetesServiceUtil {

    public static List<String> getImageNames(List<KubernetesService> ksList) {
        return ksList.stream().map(ks -> ks.getImage()).collect(Collectors.toList());
    }

    public static List<String> getEnvironmentVariableNames(List<KubernetesService> ksList) {
        List<String> envNames = new LinkedList<>();
        ksList.stream().forEach(ks -> ks.getEnvironmentVariables().forEach(env -> envNames.add(env.getName())));
        return envNames;
    }

    public static List<String> getVolumeNames(List<KubernetesService> ksList) {
        List<String> volumeNames = new LinkedList<>();
        ksList.
