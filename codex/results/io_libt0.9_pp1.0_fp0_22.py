import io.reactivex.Flowable;
import io.reactivex.schedulers.Schedulers;
import toml.langserver.Constants;
import toml.langserver.jls.ClientService;
import toml.langserver.jls.TomlDocumentService;

import java.util.Objects;
import java.util.concurrent.CompletableFuture;

public class TomlDocumentSymbolService extends TomlDocumentService {
    public TomlDocumentSymbolService(LanguageServer server) {
        super(server);
    }

    @Override
    public CompletableFuture<DocumentSymbol> handle(DocumentSymbolParams params) {
        return getServer()
                .getClient()
                .async(ClientService::registerCapability, server().getInitParams().getRegistration().getDocumentSymbol()
                .getId())
                .thenApply(it -> {
                    Document doc = params.getTextDocument();
                    return new DocumentSymbolParams(new TextDocumentIdentifier(doc.getUri()), doc.getVersion());
                })

