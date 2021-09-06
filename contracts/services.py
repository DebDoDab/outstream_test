from contracts.schemas import (
    GoogleDoc,
    GoogleDocReplacement,
    ContractReplacementsFields,
    ContractReplacements,
)


def get_template_contract() -> GoogleDoc:
    """Return template google document"""
    pass


def copy_google_doc(document: GoogleDoc) -> GoogleDoc:
    """Copies google document and returns copied google document info"""
    pass


def replace_text_google_doc(
    document: GoogleDoc, replacements: list[GoogleDocReplacement]
):
    """Replaces text in google document using replacements"""
    pass


def download_pdf_google_doc(document: GoogleDoc) -> bytes:
    """Downloads google document and returns it in base64"""
    pass


def format_replacements(
    replacements: ContractReplacements,
) -> list[GoogleDocReplacement]:
    """
    Formats replacements from request body fields to list of google document replacements
    using ContractReplacementsFields
    """
    pass


def delete_google_doc(document: GoogleDoc):
    """Deletes google doc"""
    pass


def get_pdf_contract(replacements: ContractReplacements) -> bytes:
    """
    Copies google document contract template, replaces text, downloads it, deletes copy and returns contract in base64
    """
    template_doc = get_template_contract()
    copied_doc = copy_google_doc(document=template_doc)
    replacements = format_replacements(replacements)
    copied_doc = replace_text_google_doc(copied_doc, replacements)
    file = download_pdf_google_doc(copied_doc)
    delete_google_doc(copied_doc)
    return file
