def runtime_lavamoat_cache_editor(cache_path, delete=False):
    """
    This function deletes the cache file for lavamoat.

    Args:
        cache_path (str): The path to the cache file.
        delete (bool): Whether to delete the cache file.
    """
    if delete:
        try:
            os.remove(cache_path)
            print(f"Deleted cache file {cache_path}")
        except FileNotFoundError:
            print(f"Cache file {cache_path} not found")
    else:
        with open(cache_path, "w") as f:
            f.write("1")
            print(f"Created cache file {cache_path}")

