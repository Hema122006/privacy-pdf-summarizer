def blur_text(text, pii_list):

    protected_text = text

    for item in pii_list:

        if item.strip():

            protected_text = protected_text.replace(
                item,
                "████████"
            )

    return protected_text