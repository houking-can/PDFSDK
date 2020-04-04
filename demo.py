import FoxitQPLDLL1711 as FoxitQuick

qp = FoxitQuick.PDFLibrary()
licenseKey = "..."
if qp.UnlockKey(licenseKey) == 1:
    text = qp.ExtractFilePageText('a.pdf', '', 1, 0)
    # See api document for details
