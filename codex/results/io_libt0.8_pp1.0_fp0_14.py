import io.github.fukkitmc.fukkit.redirects.RecipeManagerRedirects;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.Recipe;

public interface ShapedRecipeRedirects extends RecipeRedirects, RecipeManagerRedirects {

    static boolean equals_old(Recipe var0, Object var1) {
        if (var1 == null) {
            return false;
        } else if (!(var1 instanceof ShapedRecipe)) {
            return false;
        } else {
            ShapedRecipe var2 = (ShapedRecipe)var1;
            return var0.getResult().equals(var2.getResult()) ? true : false;
        }
    }

    static int hashCode_old(ShapedRecipe var0) {
        int var1 = 7;
        var1 = var1 * 31 + (var0.getResult().getType().hashCode() * 31 + var0.getResult().getAmount());
        return var1;
    }

    static Recipe toBukkitRecipe(Recipe var0) {
