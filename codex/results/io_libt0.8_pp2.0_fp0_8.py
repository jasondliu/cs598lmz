import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.Accessors;
import rikka.api.command.CommandSource;
import rikka.api.entity.living.player.User;
import rikka.command.Command;
import rikka.command.exception.CommandException;
import rikka.command.parameter.Parameter;
import rikka.core.util.formatting.TextFormat;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@NoArgsConstructor
@Accessors(fluent = true)
@Data
@AllArgsConstructor
public abstract class CommandSourceImpl implements CommandSource {

    private User user;
    private String id;

    @Override
    public CommandSource setUserOptional
