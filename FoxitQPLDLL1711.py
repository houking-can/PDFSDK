# Foxit Quick PDF Library
# Windows DLL Edition
# Version 17.11

# Copyright (c) 1999 - 2019 Foxit Software

# DebenuPDFLibraryCP1711.py
# Python import class
# http://www.debenu.com/

import ctypes as C
import os.path
import struct

class PDFLibrary:
  instanceID = 0
  dpl = None

  def __init__(self, pathOrFile = None):
    if pathOrFile is None:
      if 8 * struct.calcsize("P") == 32:
        dplFile = "DebenuPDFLibraryDLL1711.dll"
      else:
        dplFile = "DebenuPDFLibrary64DLL1711.dll"
    else:
      if os.path.isfile(pathOrFile):
         dplFile = pathOrFile
      if os.path.isdir(pathOrFile):
        if 8 * struct.calcsize("P") == 32:
          dplFile = os.path.join(pathOrFile, "DebenuPDFLibraryDLL1711.dll")
        else:
          dplFile = os.path.join(pathOrFile, "DebenuPDFLibrary64DLL1711.dll")
    self.dpl = C.windll.LoadLibrary(dplFile)
    self.dpl.DPLCreateLibrary.argtypes = []
    self.dpl.DPLCreateLibrary.restype = C.c_int
    self.dpl.DPLStringResultLength.argtypes = [C.c_int]
    self.dpl.DPLStringResultLength.restype = C.c_int
    self.dpl.DPLAddArcToPath.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLAddArcToPath.restype = C.c_int
    self.dpl.DPLAddBoxToPath.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLAddBoxToPath.restype = C.c_int
    self.dpl.DPLAddCJKFont.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLAddCJKFont.restype = C.c_int
    self.dpl.DPLAddCurveToPath.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLAddCurveToPath.restype = C.c_int
    self.dpl.DPLAddEmbeddedFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLAddEmbeddedFile.restype = C.c_int
    self.dpl.DPLAddFileAttachment.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddFileAttachment.restype = C.c_int
    self.dpl.DPLAddFormFieldChoiceSub.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLAddFormFieldChoiceSub.restype = C.c_int
    self.dpl.DPLAddFormFieldSub.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLAddFormFieldSub.restype = C.c_int
    self.dpl.DPLAddFormFieldSubEx.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddFormFieldSubEx.restype = C.c_int
    self.dpl.DPLAddFormFont.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLAddFormFont.restype = C.c_int
    self.dpl.DPLAddFreeTextAnnotation.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLAddFreeTextAnnotation.restype = C.c_int
    self.dpl.DPLAddFreeTextAnnotationEx.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLAddFreeTextAnnotationEx.restype = C.c_int
    self.dpl.DPLAddGlobalJavaScript.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLAddGlobalJavaScript.restype = C.c_int
    self.dpl.DPLAddImageFromFile.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddImageFromFile.restype = C.c_int
    self.dpl.DPLAddImageFromFileOffset.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLAddImageFromFileOffset.restype = C.c_int
    self.dpl.DPLAddImageFromString.argtypes = [C.c_int, C.c_void_p, C.c_int]
    self.dpl.DPLAddImageFromString.restype = C.c_int
    self.dpl.DPLAddLGIDictToPage.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLAddLGIDictToPage.restype = C.c_int
    self.dpl.DPLAddLineToPath.argtypes = [C.c_int, C.c_double, C.c_double]
    self.dpl.DPLAddLineToPath.restype = C.c_int
    self.dpl.DPLAddLinkToDestination.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLAddLinkToDestination.restype = C.c_int
    self.dpl.DPLAddLinkToEmbeddedFile.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLAddLinkToEmbeddedFile.restype = C.c_int
    self.dpl.DPLAddLinkToFile.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLAddLinkToFile.restype = C.c_int
    self.dpl.DPLAddLinkToFileDest.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_wchar_p, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLAddLinkToFileDest.restype = C.c_int
    self.dpl.DPLAddLinkToFileEx.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLAddLinkToFileEx.restype = C.c_int
    self.dpl.DPLAddLinkToJavaScript.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddLinkToJavaScript.restype = C.c_int
    self.dpl.DPLAddLinkToLocalFile.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddLinkToLocalFile.restype = C.c_int
    self.dpl.DPLAddLinkToPage.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int, C.c_double, C.c_int]
    self.dpl.DPLAddLinkToPage.restype = C.c_int
    self.dpl.DPLAddLinkToWeb.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddLinkToWeb.restype = C.c_int
    self.dpl.DPLAddNoteAnnotation.argtypes = [C.c_int, C.c_double, C.c_double, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLAddNoteAnnotation.restype = C.c_int
    self.dpl.DPLAddOpenTypeFontFromFile.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddOpenTypeFontFromFile.restype = C.c_int
    self.dpl.DPLAddOpenTypeFontFromString.argtypes = [C.c_int, C.c_void_p, C.c_int]
    self.dpl.DPLAddOpenTypeFontFromString.restype = C.c_int
    self.dpl.DPLAddPageLabels.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLAddPageLabels.restype = C.c_int
    self.dpl.DPLAddPageMatrix.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLAddPageMatrix.restype = C.c_int
    self.dpl.DPLAddRGBSeparationColor.argtypes = [C.c_int, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLAddRGBSeparationColor.restype = C.c_int
    self.dpl.DPLAddRelativeLinkToFile.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLAddRelativeLinkToFile.restype = C.c_int
    self.dpl.DPLAddRelativeLinkToFileDest.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_wchar_p, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLAddRelativeLinkToFileDest.restype = C.c_int
    self.dpl.DPLAddRelativeLinkToFileEx.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLAddRelativeLinkToFileEx.restype = C.c_int
    self.dpl.DPLAddRelativeLinkToLocalFile.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddRelativeLinkToLocalFile.restype = C.c_int
    self.dpl.DPLAddSVGAnnotationFromFile.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddSVGAnnotationFromFile.restype = C.c_int
    self.dpl.DPLAddSWFAnnotationFromFile.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddSWFAnnotationFromFile.restype = C.c_int
    self.dpl.DPLAddSeparationColor.argtypes = [C.c_int, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLAddSeparationColor.restype = C.c_int
    self.dpl.DPLAddSignProcessOverlayText.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLAddSignProcessOverlayText.restype = C.c_int
    self.dpl.DPLAddStampAnnotation.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLAddStampAnnotation.restype = C.c_int
    self.dpl.DPLAddStampAnnotationFromImage.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLAddStampAnnotationFromImage.restype = C.c_int
    self.dpl.DPLAddStampAnnotationFromImageID.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLAddStampAnnotationFromImageID.restype = C.c_int
    self.dpl.DPLAddStandardFont.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLAddStandardFont.restype = C.c_int
    self.dpl.DPLAddSubsettedFont.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_wchar_p]
    self.dpl.DPLAddSubsettedFont.restype = C.c_int
    self.dpl.DPLAddTextMarkupAnnotation.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLAddTextMarkupAnnotation.restype = C.c_int
    self.dpl.DPLAddToBuffer.argtypes = [C.c_int, C.c_void_p, C.c_void_p, C.c_int]
    self.dpl.DPLAddToBuffer.restype = C.c_int
    self.dpl.DPLAddToFileList.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLAddToFileList.restype = C.c_int
    self.dpl.DPLAddToUnicodeFontGroup.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddToUnicodeFontGroup.restype = C.c_int
    self.dpl.DPLAddTrueTypeFont.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddTrueTypeFont.restype = C.c_int
    self.dpl.DPLAddTrueTypeFontFromFile.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLAddTrueTypeFontFromFile.restype = C.c_int
    self.dpl.DPLAddTrueTypeFontFromFileEx.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddTrueTypeFontFromFileEx.restype = C.c_int
    self.dpl.DPLAddTrueTypeFontFromString.argtypes = [C.c_int, C.c_void_p]
    self.dpl.DPLAddTrueTypeFontFromString.restype = C.c_int
    self.dpl.DPLAddTrueTypeFontFromStringEx.argtypes = [C.c_int, C.c_void_p, C.c_int]
    self.dpl.DPLAddTrueTypeFontFromStringEx.restype = C.c_int
    self.dpl.DPLAddTrueTypeSubsettedFont.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddTrueTypeSubsettedFont.restype = C.c_int
    self.dpl.DPLAddTrueTypeSubsettedFontFromFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddTrueTypeSubsettedFontFromFile.restype = C.c_int
    self.dpl.DPLAddTrueTypeSubsettedFontFromString.argtypes = [C.c_int, C.c_void_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddTrueTypeSubsettedFontFromString.restype = C.c_int
    self.dpl.DPLAddType1Font.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLAddType1Font.restype = C.c_int
    self.dpl.DPLAddU3DAnnotationFromFile.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLAddU3DAnnotationFromFile.restype = C.c_int
    self.dpl.DPLAddUnicodeFont.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLAddUnicodeFont.restype = C.c_int
    self.dpl.DPLAddUnicodeFontFromFile.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLAddUnicodeFontFromFile.restype = C.c_int
    self.dpl.DPLAnalyseFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLAnalyseFile.restype = C.c_int
    self.dpl.DPLAnnotationCount.argtypes = [C.c_int]
    self.dpl.DPLAnnotationCount.restype = C.c_int
    self.dpl.DPLAnsiStringResultLength.argtypes = [C.c_int]
    self.dpl.DPLAnsiStringResultLength.restype = C.c_int
    self.dpl.DPLAppendSpace.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLAppendSpace.restype = C.c_int
    self.dpl.DPLAppendTableColumns.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLAppendTableColumns.restype = C.c_int
    self.dpl.DPLAppendTableRows.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLAppendTableRows.restype = C.c_int
    self.dpl.DPLAppendText.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLAppendText.restype = C.c_int
    self.dpl.DPLAppendToFile.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLAppendToFile.restype = C.c_int
    self.dpl.DPLAppendToString.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLAppendToString.restype = C.c_void_p
    self.dpl.DPLApplyStyle.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLApplyStyle.restype = C.c_int
    self.dpl.DPLAttachAnnotToForm.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLAttachAnnotToForm.restype = C.c_int
    self.dpl.DPLBalanceContentStream.argtypes = [C.c_int]
    self.dpl.DPLBalanceContentStream.restype = C.c_int
    self.dpl.DPLBalancePageTree.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLBalancePageTree.restype = C.c_int
    self.dpl.DPLBeginPageUpdate.argtypes = [C.c_int]
    self.dpl.DPLBeginPageUpdate.restype = C.c_int
    self.dpl.DPLCapturePage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLCapturePage.restype = C.c_int
    self.dpl.DPLCapturePageEx.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLCapturePageEx.restype = C.c_int
    self.dpl.DPLCharWidth.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLCharWidth.restype = C.c_int
    self.dpl.DPLCheckFileCompliance.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLCheckFileCompliance.restype = C.c_int
    self.dpl.DPLCheckObjects.argtypes = [C.c_int]
    self.dpl.DPLCheckObjects.restype = C.c_int
    self.dpl.DPLCheckPageAnnots.argtypes = [C.c_int]
    self.dpl.DPLCheckPageAnnots.restype = C.c_int
    self.dpl.DPLCheckPassword.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLCheckPassword.restype = C.c_int
    self.dpl.DPLClearFileList.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLClearFileList.restype = C.c_int
    self.dpl.DPLClearImage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLClearImage.restype = C.c_int
    self.dpl.DPLClearPageLabels.argtypes = [C.c_int]
    self.dpl.DPLClearPageLabels.restype = C.c_int
    self.dpl.DPLClearTextFormatting.argtypes = [C.c_int]
    self.dpl.DPLClearTextFormatting.restype = C.c_int
    self.dpl.DPLCloneOutlineAction.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLCloneOutlineAction.restype = C.c_int
    self.dpl.DPLClonePages.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLClonePages.restype = C.c_int
    self.dpl.DPLCloseOutline.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLCloseOutline.restype = C.c_int
    self.dpl.DPLClosePath.argtypes = [C.c_int]
    self.dpl.DPLClosePath.restype = C.c_int
    self.dpl.DPLCombineContentStreams.argtypes = [C.c_int]
    self.dpl.DPLCombineContentStreams.restype = C.c_int
    self.dpl.DPLCompareOutlines.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLCompareOutlines.restype = C.c_int
    self.dpl.DPLCompressContent.argtypes = [C.c_int]
    self.dpl.DPLCompressContent.restype = C.c_int
    self.dpl.DPLCompressFonts.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLCompressFonts.restype = C.c_int
    self.dpl.DPLCompressImages.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLCompressImages.restype = C.c_int
    self.dpl.DPLCompressPage.argtypes = [C.c_int]
    self.dpl.DPLCompressPage.restype = C.c_int
    self.dpl.DPLContentStreamCount.argtypes = [C.c_int]
    self.dpl.DPLContentStreamCount.restype = C.c_int
    self.dpl.DPLContentStreamSafe.argtypes = [C.c_int]
    self.dpl.DPLContentStreamSafe.restype = C.c_int
    self.dpl.DPLCopyPageRanges.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLCopyPageRanges.restype = C.c_int
    self.dpl.DPLCopyPageRangesEx.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLCopyPageRangesEx.restype = C.c_int
    self.dpl.DPLCreateBuffer.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLCreateBuffer.restype = C.c_void_p
    self.dpl.DPLCreateNewObject.argtypes = [C.c_int]
    self.dpl.DPLCreateNewObject.restype = C.c_int
    self.dpl.DPLCreateRenderer.argtypes = [C.c_int]
    self.dpl.DPLCreateRenderer.restype = C.c_int
    self.dpl.DPLCreateTable.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLCreateTable.restype = C.c_int
    self.dpl.DPLDAAppendFile.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAAppendFile.restype = C.c_int
    self.dpl.DPLDACapturePage.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDACapturePage.restype = C.c_int
    self.dpl.DPLDACapturePageEx.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDACapturePageEx.restype = C.c_int
    self.dpl.DPLDACloseFile.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDACloseFile.restype = C.c_int
    self.dpl.DPLDADrawCapturedPage.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDADrawCapturedPage.restype = C.c_int
    self.dpl.DPLDADrawRotatedCapturedPage.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDADrawRotatedCapturedPage.restype = C.c_int
    self.dpl.DPLDAEmbedFileStreams.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLDAEmbedFileStreams.restype = C.c_int
    self.dpl.DPLDAExtractPageText.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAExtractPageText.restype = C.c_wchar_p
    self.dpl.DPLDAExtractPageTextBlocks.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAExtractPageTextBlocks.restype = C.c_int
    self.dpl.DPLDAFindPage.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAFindPage.restype = C.c_int
    self.dpl.DPLDAGetAnnotationCount.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetAnnotationCount.restype = C.c_int
    self.dpl.DPLDAGetFormFieldCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAGetFormFieldCount.restype = C.c_int
    self.dpl.DPLDAGetFormFieldTitle.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetFormFieldTitle.restype = C.c_wchar_p
    self.dpl.DPLDAGetFormFieldValue.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetFormFieldValue.restype = C.c_wchar_p
    self.dpl.DPLDAGetImageDataToString.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetImageDataToString.restype = C.c_void_p
    self.dpl.DPLDAGetImageDblProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetImageDblProperty.restype = C.c_double
    self.dpl.DPLDAGetImageIntProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetImageIntProperty.restype = C.c_int
    self.dpl.DPLDAGetImageListCount.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetImageListCount.restype = C.c_int
    self.dpl.DPLDAGetInformation.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLDAGetInformation.restype = C.c_wchar_p
    self.dpl.DPLDAGetObjectCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAGetObjectCount.restype = C.c_int
    self.dpl.DPLDAGetObjectToString.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetObjectToString.restype = C.c_void_p
    self.dpl.DPLDAGetPageBox.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetPageBox.restype = C.c_double
    self.dpl.DPLDAGetPageContentToString.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetPageContentToString.restype = C.c_void_p
    self.dpl.DPLDAGetPageCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAGetPageCount.restype = C.c_int
    self.dpl.DPLDAGetPageHeight.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetPageHeight.restype = C.c_double
    self.dpl.DPLDAGetPageImageList.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetPageImageList.restype = C.c_int
    self.dpl.DPLDAGetPageLayout.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAGetPageLayout.restype = C.c_int
    self.dpl.DPLDAGetPageMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAGetPageMode.restype = C.c_int
    self.dpl.DPLDAGetPageWidth.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetPageWidth.restype = C.c_double
    self.dpl.DPLDAGetTextBlockAsString.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockAsString.restype = C.c_wchar_p
    self.dpl.DPLDAGetTextBlockBound.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockBound.restype = C.c_double
    self.dpl.DPLDAGetTextBlockCharWidth.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockCharWidth.restype = C.c_double
    self.dpl.DPLDAGetTextBlockColor.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockColor.restype = C.c_double
    self.dpl.DPLDAGetTextBlockColorType.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockColorType.restype = C.c_int
    self.dpl.DPLDAGetTextBlockCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockCount.restype = C.c_int
    self.dpl.DPLDAGetTextBlockFontName.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockFontName.restype = C.c_wchar_p
    self.dpl.DPLDAGetTextBlockFontSize.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockFontSize.restype = C.c_double
    self.dpl.DPLDAGetTextBlockText.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAGetTextBlockText.restype = C.c_wchar_p
    self.dpl.DPLDAHasPageBox.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAHasPageBox.restype = C.c_int
    self.dpl.DPLDAHidePage.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAHidePage.restype = C.c_int
    self.dpl.DPLDAMovePage.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAMovePage.restype = C.c_int
    self.dpl.DPLDANewPage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDANewPage.restype = C.c_int
    self.dpl.DPLDANewPages.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDANewPages.restype = C.c_int
    self.dpl.DPLDANormalizePage.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDANormalizePage.restype = C.c_int
    self.dpl.DPLDAOpenFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLDAOpenFile.restype = C.c_int
    self.dpl.DPLDAOpenFileReadOnly.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLDAOpenFileReadOnly.restype = C.c_int
    self.dpl.DPLDAPageRotation.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAPageRotation.restype = C.c_int
    self.dpl.DPLDAReleaseImageList.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDAReleaseImageList.restype = C.c_int
    self.dpl.DPLDAReleaseTextBlocks.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAReleaseTextBlocks.restype = C.c_int
    self.dpl.DPLDARemoveUsageRights.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDARemoveUsageRights.restype = C.c_int
    self.dpl.DPLDARenderPageToDC.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, ]
    self.dpl.DPLDARenderPageToDC.restype = C.c_int
    self.dpl.DPLDARenderPageToFile.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_wchar_p]
    self.dpl.DPLDARenderPageToFile.restype = C.c_int
    self.dpl.DPLDARenderPageToString.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLDARenderPageToString.restype = C.c_void_p
    self.dpl.DPLDARotatePage.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDARotatePage.restype = C.c_int
    self.dpl.DPLDASaveAsFile.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLDASaveAsFile.restype = C.c_int
    self.dpl.DPLDASaveImageDataToFile.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLDASaveImageDataToFile.restype = C.c_int
    self.dpl.DPLDASetInformation.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLDASetInformation.restype = C.c_int
    self.dpl.DPLDASetPageBox.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDASetPageBox.restype = C.c_int
    self.dpl.DPLDASetPageLayout.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDASetPageLayout.restype = C.c_int
    self.dpl.DPLDASetPageMode.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDASetPageMode.restype = C.c_int
    self.dpl.DPLDASetPageSize.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, C.c_double]
    self.dpl.DPLDASetPageSize.restype = C.c_int
    self.dpl.DPLDASetRenderArea.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDASetRenderArea.restype = C.c_int
    self.dpl.DPLDASetTextExtractionArea.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDASetTextExtractionArea.restype = C.c_int
    self.dpl.DPLDASetTextExtractionOptions.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDASetTextExtractionOptions.restype = C.c_int
    self.dpl.DPLDASetTextExtractionScaling.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double]
    self.dpl.DPLDASetTextExtractionScaling.restype = C.c_int
    self.dpl.DPLDASetTextExtractionWordGap.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLDASetTextExtractionWordGap.restype = C.c_int
    self.dpl.DPLDAShiftedHeader.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDAShiftedHeader.restype = C.c_int
    self.dpl.DPLDecrypt.argtypes = [C.c_int]
    self.dpl.DPLDecrypt.restype = C.c_int
    self.dpl.DPLDecryptFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLDecryptFile.restype = C.c_int
    self.dpl.DPLDeleteAnalysis.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDeleteAnalysis.restype = C.c_int
    self.dpl.DPLDeleteAnnotation.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDeleteAnnotation.restype = C.c_int
    self.dpl.DPLDeleteContentStream.argtypes = [C.c_int]
    self.dpl.DPLDeleteContentStream.restype = C.c_int
    self.dpl.DPLDeleteFormField.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDeleteFormField.restype = C.c_int
    self.dpl.DPLDeleteOptionalContentGroup.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDeleteOptionalContentGroup.restype = C.c_int
    self.dpl.DPLDeletePageLGIDict.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDeletePageLGIDict.restype = C.c_int
    self.dpl.DPLDeletePages.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDeletePages.restype = C.c_int
    self.dpl.DPLDestroyRenderer.argtypes = [C.c_int]
    self.dpl.DPLDestroyRenderer.restype = C.c_int
    self.dpl.DPLDocJavaScriptAction.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLDocJavaScriptAction.restype = C.c_int
    self.dpl.DPLDocumentCount.argtypes = [C.c_int]
    self.dpl.DPLDocumentCount.restype = C.c_int
    self.dpl.DPLDrawArc.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLDrawArc.restype = C.c_int
    self.dpl.DPLDrawBarcode.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLDrawBarcode.restype = C.c_int
    self.dpl.DPLDrawBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLDrawBox.restype = C.c_int
    self.dpl.DPLDrawCapturedPage.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawCapturedPage.restype = C.c_int
    self.dpl.DPLDrawCapturedPageMatrix.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawCapturedPageMatrix.restype = C.c_int
    self.dpl.DPLDrawCircle.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLDrawCircle.restype = C.c_int
    self.dpl.DPLDrawDataMatrixSymbol.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDrawDataMatrixSymbol.restype = C.c_int
    self.dpl.DPLDrawEllipse.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLDrawEllipse.restype = C.c_int
    self.dpl.DPLDrawEllipticArc.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLDrawEllipticArc.restype = C.c_int
    self.dpl.DPLDrawFontGroupText.argtypes = [C.c_int, C.c_wchar_p, C.c_double, C.c_double, C.c_wchar_p]
    self.dpl.DPLDrawFontGroupText.restype = C.c_int
    self.dpl.DPLDrawHTMLText.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_wchar_p]
    self.dpl.DPLDrawHTMLText.restype = C.c_int
    self.dpl.DPLDrawHTMLTextBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p]
    self.dpl.DPLDrawHTMLTextBox.restype = C.c_wchar_p
    self.dpl.DPLDrawHTMLTextBoxMatrix.argtypes = [C.c_int, C.c_double, C.c_double, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawHTMLTextBoxMatrix.restype = C.c_wchar_p
    self.dpl.DPLDrawHTMLTextMatrix.argtypes = [C.c_int, C.c_double, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawHTMLTextMatrix.restype = C.c_int
    self.dpl.DPLDrawImage.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawImage.restype = C.c_int
    self.dpl.DPLDrawImageMatrix.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawImageMatrix.restype = C.c_int
    self.dpl.DPLDrawIntelligentMailBarcode.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLDrawIntelligentMailBarcode.restype = C.c_int
    self.dpl.DPLDrawLine.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawLine.restype = C.c_int
    self.dpl.DPLDrawMultiLineText.argtypes = [C.c_int, C.c_double, C.c_double, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLDrawMultiLineText.restype = C.c_int
    self.dpl.DPLDrawPDF417Symbol.argtypes = [C.c_int, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLDrawPDF417Symbol.restype = C.c_int
    self.dpl.DPLDrawPDF417SymbolEx.argtypes = [C.c_int, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double]
    self.dpl.DPLDrawPDF417SymbolEx.restype = C.c_int
    self.dpl.DPLDrawPath.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDrawPath.restype = C.c_int
    self.dpl.DPLDrawPathEvenOdd.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDrawPathEvenOdd.restype = C.c_int
    self.dpl.DPLDrawPostScriptXObject.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLDrawPostScriptXObject.restype = C.c_int
    self.dpl.DPLDrawQRCode.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLDrawQRCode.restype = C.c_int
    self.dpl.DPLDrawRotatedBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLDrawRotatedBox.restype = C.c_int
    self.dpl.DPLDrawRotatedCapturedPage.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawRotatedCapturedPage.restype = C.c_int
    self.dpl.DPLDrawRotatedImage.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawRotatedImage.restype = C.c_int
    self.dpl.DPLDrawRotatedMultiLineText.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLDrawRotatedMultiLineText.restype = C.c_int
    self.dpl.DPLDrawRotatedText.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_wchar_p]
    self.dpl.DPLDrawRotatedText.restype = C.c_int
    self.dpl.DPLDrawRotatedTextBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLDrawRotatedTextBox.restype = C.c_int
    self.dpl.DPLDrawRotatedTextBoxEx.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLDrawRotatedTextBoxEx.restype = C.c_int
    self.dpl.DPLDrawRoundedBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLDrawRoundedBox.restype = C.c_int
    self.dpl.DPLDrawRoundedRotatedBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLDrawRoundedRotatedBox.restype = C.c_int
    self.dpl.DPLDrawScaledImage.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawScaledImage.restype = C.c_int
    self.dpl.DPLDrawSpacedText.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_wchar_p]
    self.dpl.DPLDrawSpacedText.restype = C.c_int
    self.dpl.DPLDrawTableRows.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLDrawTableRows.restype = C.c_double
    self.dpl.DPLDrawText.argtypes = [C.c_int, C.c_double, C.c_double, C.c_wchar_p]
    self.dpl.DPLDrawText.restype = C.c_int
    self.dpl.DPLDrawTextArc.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLDrawTextArc.restype = C.c_int
    self.dpl.DPLDrawTextBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLDrawTextBox.restype = C.c_int
    self.dpl.DPLDrawTextBoxMatrix.argtypes = [C.c_int, C.c_double, C.c_double, C.c_wchar_p, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLDrawTextBoxMatrix.restype = C.c_int
    self.dpl.DPLDrawUniscribeText.argtypes = [C.c_int, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLDrawUniscribeText.restype = C.c_int
    self.dpl.DPLDrawWrappedText.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_wchar_p]
    self.dpl.DPLDrawWrappedText.restype = C.c_int
    self.dpl.DPLEditableContentStream.argtypes = [C.c_int]
    self.dpl.DPLEditableContentStream.restype = C.c_int
    self.dpl.DPLEmbedFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLEmbedFile.restype = C.c_int
    self.dpl.DPLEmbedRelatedFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLEmbedRelatedFile.restype = C.c_int
    self.dpl.DPLEmbeddedFileCount.argtypes = [C.c_int]
    self.dpl.DPLEmbeddedFileCount.restype = C.c_int
    self.dpl.DPLEncapsulateContentStream.argtypes = [C.c_int]
    self.dpl.DPLEncapsulateContentStream.restype = C.c_int
    self.dpl.DPLEncodePermissions.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLEncodePermissions.restype = C.c_int
    self.dpl.DPLEncrypt.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLEncrypt.restype = C.c_int
    self.dpl.DPLEncryptFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLEncryptFile.restype = C.c_int
    self.dpl.DPLEncryptWithFingerprint.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLEncryptWithFingerprint.restype = C.c_int
    self.dpl.DPLEncryptionAlgorithm.argtypes = [C.c_int]
    self.dpl.DPLEncryptionAlgorithm.restype = C.c_int
    self.dpl.DPLEncryptionStatus.argtypes = [C.c_int]
    self.dpl.DPLEncryptionStatus.restype = C.c_int
    self.dpl.DPLEncryptionStrength.argtypes = [C.c_int]
    self.dpl.DPLEncryptionStrength.restype = C.c_int
    self.dpl.DPLEndPageUpdate.argtypes = [C.c_int]
    self.dpl.DPLEndPageUpdate.restype = C.c_int
    self.dpl.DPLEndSignProcessToFile.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLEndSignProcessToFile.restype = C.c_int
    self.dpl.DPLEndSignProcessToString.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLEndSignProcessToString.restype = C.c_void_p
    self.dpl.DPLExtractFilePageContentToString.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLExtractFilePageContentToString.restype = C.c_void_p
    self.dpl.DPLExtractFilePageText.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLExtractFilePageText.restype = C.c_wchar_p
    self.dpl.DPLExtractFilePageTextBlocks.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLExtractFilePageTextBlocks.restype = C.c_int
    self.dpl.DPLExtractFilePages.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLExtractFilePages.restype = C.c_int
    self.dpl.DPLExtractFilePagesEx.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLExtractFilePagesEx.restype = C.c_int
    self.dpl.DPLExtractPageRanges.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLExtractPageRanges.restype = C.c_int
    self.dpl.DPLExtractPageTextBlocks.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLExtractPageTextBlocks.restype = C.c_int
    self.dpl.DPLExtractPages.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLExtractPages.restype = C.c_int
    self.dpl.DPLFileListCount.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLFileListCount.restype = C.c_int
    self.dpl.DPLFileListItem.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLFileListItem.restype = C.c_wchar_p
    self.dpl.DPLFindFonts.argtypes = [C.c_int]
    self.dpl.DPLFindFonts.restype = C.c_int
    self.dpl.DPLFindFormFieldByTitle.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLFindFormFieldByTitle.restype = C.c_int
    self.dpl.DPLFindImages.argtypes = [C.c_int]
    self.dpl.DPLFindImages.restype = C.c_int
    self.dpl.DPLFitImage.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLFitImage.restype = C.c_int
    self.dpl.DPLFitRotatedTextBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLFitRotatedTextBox.restype = C.c_int
    self.dpl.DPLFitTextBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLFitTextBox.restype = C.c_int
    self.dpl.DPLFlattenAllFormFields.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLFlattenAllFormFields.restype = C.c_int
    self.dpl.DPLFlattenAnnot.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLFlattenAnnot.restype = C.c_int
    self.dpl.DPLFlattenFormField.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLFlattenFormField.restype = C.c_int
    self.dpl.DPLFontCount.argtypes = [C.c_int]
    self.dpl.DPLFontCount.restype = C.c_int
    self.dpl.DPLFontFamily.argtypes = [C.c_int]
    self.dpl.DPLFontFamily.restype = C.c_wchar_p
    self.dpl.DPLFontHasKerning.argtypes = [C.c_int]
    self.dpl.DPLFontHasKerning.restype = C.c_int
    self.dpl.DPLFontName.argtypes = [C.c_int]
    self.dpl.DPLFontName.restype = C.c_wchar_p
    self.dpl.DPLFontReference.argtypes = [C.c_int]
    self.dpl.DPLFontReference.restype = C.c_wchar_p
    self.dpl.DPLFontSize.argtypes = [C.c_int]
    self.dpl.DPLFontSize.restype = C.c_int
    self.dpl.DPLFontType.argtypes = [C.c_int]
    self.dpl.DPLFontType.restype = C.c_int
    self.dpl.DPLFormFieldCount.argtypes = [C.c_int]
    self.dpl.DPLFormFieldCount.restype = C.c_int
    self.dpl.DPLFormFieldHasParent.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLFormFieldHasParent.restype = C.c_int
    self.dpl.DPLFormFieldJavaScriptAction.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLFormFieldJavaScriptAction.restype = C.c_int
    self.dpl.DPLFormFieldWebLinkAction.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLFormFieldWebLinkAction.restype = C.c_int
    self.dpl.DPLGetActionDest.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetActionDest.restype = C.c_int
    self.dpl.DPLGetActionType.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetActionType.restype = C.c_wchar_p
    self.dpl.DPLGetActionURL.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetActionURL.restype = C.c_wchar_p
    self.dpl.DPLGetAnalysisInfo.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetAnalysisInfo.restype = C.c_wchar_p
    self.dpl.DPLGetAnnotActionID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetAnnotActionID.restype = C.c_int
    self.dpl.DPLGetAnnotDblProperty.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetAnnotDblProperty.restype = C.c_double
    self.dpl.DPLGetAnnotDest.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetAnnotDest.restype = C.c_int
    self.dpl.DPLGetAnnotEmbeddedFileName.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetAnnotEmbeddedFileName.restype = C.c_wchar_p
    self.dpl.DPLGetAnnotEmbeddedFileToFile.argtypes = [C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLGetAnnotEmbeddedFileToFile.restype = C.c_int
    self.dpl.DPLGetAnnotEmbeddedFileToString.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetAnnotEmbeddedFileToString.restype = C.c_void_p
    self.dpl.DPLGetAnnotIntProperty.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetAnnotIntProperty.restype = C.c_int
    self.dpl.DPLGetAnnotQuadCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetAnnotQuadCount.restype = C.c_int
    self.dpl.DPLGetAnnotQuadPoints.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetAnnotQuadPoints.restype = C.c_double
    self.dpl.DPLGetAnnotSoundToFile.argtypes = [C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLGetAnnotSoundToFile.restype = C.c_int
    self.dpl.DPLGetAnnotSoundToString.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetAnnotSoundToString.restype = C.c_void_p
    self.dpl.DPLGetAnnotStrProperty.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetAnnotStrProperty.restype = C.c_wchar_p
    self.dpl.DPLGetBarcodeWidth.argtypes = [C.c_int, C.c_double, C.c_wchar_p, C.c_int]
    self.dpl.DPLGetBarcodeWidth.restype = C.c_double
    self.dpl.DPLGetBaseURL.argtypes = [C.c_int]
    self.dpl.DPLGetBaseURL.restype = C.c_wchar_p
    self.dpl.DPLGetCSDictEPSG.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetCSDictEPSG.restype = C.c_int
    self.dpl.DPLGetCSDictType.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetCSDictType.restype = C.c_int
    self.dpl.DPLGetCSDictWKT.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetCSDictWKT.restype = C.c_wchar_p
    self.dpl.DPLGetCatalogInformation.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetCatalogInformation.restype = C.c_wchar_p
    self.dpl.DPLGetContentStreamToString.argtypes = [C.c_int]
    self.dpl.DPLGetContentStreamToString.restype = C.c_void_p
    self.dpl.DPLGetCustomInformation.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetCustomInformation.restype = C.c_wchar_p
    self.dpl.DPLGetCustomKeys.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetCustomKeys.restype = C.c_wchar_p
    self.dpl.DPLGetDefaultPrinterName.argtypes = [C.c_int]
    self.dpl.DPLGetDefaultPrinterName.restype = C.c_wchar_p
    self.dpl.DPLGetDestName.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetDestName.restype = C.c_wchar_p
    self.dpl.DPLGetDestPage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetDestPage.restype = C.c_int
    self.dpl.DPLGetDestType.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetDestType.restype = C.c_int
    self.dpl.DPLGetDestValue.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetDestValue.restype = C.c_double
    self.dpl.DPLGetDocJavaScript.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetDocJavaScript.restype = C.c_wchar_p
    self.dpl.DPLGetDocumentFileName.argtypes = [C.c_int]
    self.dpl.DPLGetDocumentFileName.restype = C.c_wchar_p
    self.dpl.DPLGetDocumentFileSize.argtypes = [C.c_int]
    self.dpl.DPLGetDocumentFileSize.restype = C.c_int
    self.dpl.DPLGetDocumentID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetDocumentID.restype = C.c_int
    self.dpl.DPLGetDocumentIdentifier.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetDocumentIdentifier.restype = C.c_wchar_p
    self.dpl.DPLGetDocumentMetadata.argtypes = [C.c_int]
    self.dpl.DPLGetDocumentMetadata.restype = C.c_wchar_p
    self.dpl.DPLGetDocumentRepaired.argtypes = [C.c_int]
    self.dpl.DPLGetDocumentRepaired.restype = C.c_int
    self.dpl.DPLGetDocumentResourceList.argtypes = [C.c_int]
    self.dpl.DPLGetDocumentResourceList.restype = C.c_wchar_p
    self.dpl.DPLGetEmbeddedFileContentToFile.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLGetEmbeddedFileContentToFile.restype = C.c_int
    self.dpl.DPLGetEmbeddedFileContentToString.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetEmbeddedFileContentToString.restype = C.c_void_p
    self.dpl.DPLGetEmbeddedFileID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetEmbeddedFileID.restype = C.c_int
    self.dpl.DPLGetEmbeddedFileIntProperty.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetEmbeddedFileIntProperty.restype = C.c_int
    self.dpl.DPLGetEmbeddedFileStrProperty.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetEmbeddedFileStrProperty.restype = C.c_wchar_p
    self.dpl.DPLGetEncryptionFingerprint.argtypes = [C.c_int]
    self.dpl.DPLGetEncryptionFingerprint.restype = C.c_wchar_p
    self.dpl.DPLGetFileMetadata.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLGetFileMetadata.restype = C.c_wchar_p
    self.dpl.DPLGetFirstChildOutline.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFirstChildOutline.restype = C.c_int
    self.dpl.DPLGetFirstOutline.argtypes = [C.c_int]
    self.dpl.DPLGetFirstOutline.restype = C.c_int
    self.dpl.DPLGetFontCharacterCodesToString.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetFontCharacterCodesToString.restype = C.c_void_p
    self.dpl.DPLGetFontEncoding.argtypes = [C.c_int]
    self.dpl.DPLGetFontEncoding.restype = C.c_int
    self.dpl.DPLGetFontFlags.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFontFlags.restype = C.c_int
    self.dpl.DPLGetFontID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFontID.restype = C.c_int
    self.dpl.DPLGetFontIsEmbedded.argtypes = [C.c_int]
    self.dpl.DPLGetFontIsEmbedded.restype = C.c_int
    self.dpl.DPLGetFontIsSubsetted.argtypes = [C.c_int]
    self.dpl.DPLGetFontIsSubsetted.restype = C.c_int
    self.dpl.DPLGetFontMetrics.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFontMetrics.restype = C.c_int
    self.dpl.DPLGetFontObjectNumber.argtypes = [C.c_int]
    self.dpl.DPLGetFontObjectNumber.restype = C.c_int
    self.dpl.DPLGetFormFieldActionID.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLGetFormFieldActionID.restype = C.c_int
    self.dpl.DPLGetFormFieldAlignment.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldAlignment.restype = C.c_int
    self.dpl.DPLGetFormFieldAnnotFlags.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldAnnotFlags.restype = C.c_int
    self.dpl.DPLGetFormFieldBackgroundColor.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldBackgroundColor.restype = C.c_double
    self.dpl.DPLGetFormFieldBackgroundColorType.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldBackgroundColorType.restype = C.c_int
    self.dpl.DPLGetFormFieldBorderColor.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldBorderColor.restype = C.c_double
    self.dpl.DPLGetFormFieldBorderColorType.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldBorderColorType.restype = C.c_int
    self.dpl.DPLGetFormFieldBorderProperty.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldBorderProperty.restype = C.c_double
    self.dpl.DPLGetFormFieldBorderStyle.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldBorderStyle.restype = C.c_int
    self.dpl.DPLGetFormFieldBound.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldBound.restype = C.c_double
    self.dpl.DPLGetFormFieldCaption.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldCaption.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldCaptionEx.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldCaptionEx.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldCheckStyle.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldCheckStyle.restype = C.c_int
    self.dpl.DPLGetFormFieldChildTitle.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldChildTitle.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldChoiceType.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldChoiceType.restype = C.c_int
    self.dpl.DPLGetFormFieldColor.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldColor.restype = C.c_double
    self.dpl.DPLGetFormFieldComb.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldComb.restype = C.c_int
    self.dpl.DPLGetFormFieldDefaultValue.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldDefaultValue.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldDescription.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldDescription.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldFlags.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldFlags.restype = C.c_int
    self.dpl.DPLGetFormFieldFontName.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldFontName.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldJavaScript.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLGetFormFieldJavaScript.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldKidCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldKidCount.restype = C.c_int
    self.dpl.DPLGetFormFieldKidTempIndex.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldKidTempIndex.restype = C.c_int
    self.dpl.DPLGetFormFieldMaxLen.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldMaxLen.restype = C.c_int
    self.dpl.DPLGetFormFieldNoExport.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldNoExport.restype = C.c_int
    self.dpl.DPLGetFormFieldPage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldPage.restype = C.c_int
    self.dpl.DPLGetFormFieldPrintable.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldPrintable.restype = C.c_int
    self.dpl.DPLGetFormFieldReadOnly.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldReadOnly.restype = C.c_int
    self.dpl.DPLGetFormFieldRequired.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldRequired.restype = C.c_int
    self.dpl.DPLGetFormFieldRichTextString.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLGetFormFieldRichTextString.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldRotation.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldRotation.restype = C.c_int
    self.dpl.DPLGetFormFieldSubCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldSubCount.restype = C.c_int
    self.dpl.DPLGetFormFieldSubDisplayName.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldSubDisplayName.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldSubName.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldSubName.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldSubmitActionString.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLGetFormFieldSubmitActionString.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldTabOrder.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldTabOrder.restype = C.c_int
    self.dpl.DPLGetFormFieldTabOrderEx.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldTabOrderEx.restype = C.c_int
    self.dpl.DPLGetFormFieldTextFlags.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldTextFlags.restype = C.c_int
    self.dpl.DPLGetFormFieldTextSize.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldTextSize.restype = C.c_double
    self.dpl.DPLGetFormFieldTitle.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldTitle.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldType.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldType.restype = C.c_int
    self.dpl.DPLGetFormFieldValue.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldValue.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldValueByTitle.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetFormFieldValueByTitle.restype = C.c_wchar_p
    self.dpl.DPLGetFormFieldVisible.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFieldVisible.restype = C.c_int
    self.dpl.DPLGetFormFieldWebLink.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLGetFormFieldWebLink.restype = C.c_wchar_p
    self.dpl.DPLGetFormFontCount.argtypes = [C.c_int]
    self.dpl.DPLGetFormFontCount.restype = C.c_int
    self.dpl.DPLGetFormFontName.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetFormFontName.restype = C.c_wchar_p
    self.dpl.DPLGetGlobalJavaScript.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetGlobalJavaScript.restype = C.c_wchar_p
    self.dpl.DPLGetHTMLTextHeight.argtypes = [C.c_int, C.c_double, C.c_wchar_p]
    self.dpl.DPLGetHTMLTextHeight.restype = C.c_double
    self.dpl.DPLGetHTMLTextLineCount.argtypes = [C.c_int, C.c_double, C.c_wchar_p]
    self.dpl.DPLGetHTMLTextLineCount.restype = C.c_int
    self.dpl.DPLGetHTMLTextWidth.argtypes = [C.c_int, C.c_double, C.c_wchar_p]
    self.dpl.DPLGetHTMLTextWidth.restype = C.c_double
    self.dpl.DPLGetImageID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetImageID.restype = C.c_int
    self.dpl.DPLGetImageListCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetImageListCount.restype = C.c_int
    self.dpl.DPLGetImageListItemDataToString.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetImageListItemDataToString.restype = C.c_void_p
    self.dpl.DPLGetImageListItemDblProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetImageListItemDblProperty.restype = C.c_double
    self.dpl.DPLGetImageListItemFormatDesc.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetImageListItemFormatDesc.restype = C.c_wchar_p
    self.dpl.DPLGetImageListItemIntProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetImageListItemIntProperty.restype = C.c_int
    self.dpl.DPLGetImageMeasureDict.argtypes = [C.c_int]
    self.dpl.DPLGetImageMeasureDict.restype = C.c_int
    self.dpl.DPLGetImagePageCount.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetImagePageCount.restype = C.c_int
    self.dpl.DPLGetImagePageCountFromString.argtypes = [C.c_int, C.c_void_p]
    self.dpl.DPLGetImagePageCountFromString.restype = C.c_int
    self.dpl.DPLGetImagePtDataDict.argtypes = [C.c_int]
    self.dpl.DPLGetImagePtDataDict.restype = C.c_int
    self.dpl.DPLGetInformation.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetInformation.restype = C.c_wchar_p
    self.dpl.DPLGetInstalledFontsByCharset.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetInstalledFontsByCharset.restype = C.c_wchar_p
    self.dpl.DPLGetInstalledFontsByCodePage.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetInstalledFontsByCodePage.restype = C.c_wchar_p
    self.dpl.DPLGetKerning.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetKerning.restype = C.c_int
    self.dpl.DPLGetLatestPrinterNames.argtypes = [C.c_int]
    self.dpl.DPLGetLatestPrinterNames.restype = C.c_wchar_p
    self.dpl.DPLGetMaxObjectNumber.argtypes = [C.c_int]
    self.dpl.DPLGetMaxObjectNumber.restype = C.c_int
    self.dpl.DPLGetMeasureDictBoundsCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictBoundsCount.restype = C.c_int
    self.dpl.DPLGetMeasureDictBoundsItem.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictBoundsItem.restype = C.c_double
    self.dpl.DPLGetMeasureDictCoordinateSystem.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictCoordinateSystem.restype = C.c_int
    self.dpl.DPLGetMeasureDictDCSDict.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictDCSDict.restype = C.c_int
    self.dpl.DPLGetMeasureDictGCSDict.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictGCSDict.restype = C.c_int
    self.dpl.DPLGetMeasureDictGPTSCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictGPTSCount.restype = C.c_int
    self.dpl.DPLGetMeasureDictGPTSItem.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictGPTSItem.restype = C.c_double
    self.dpl.DPLGetMeasureDictLPTSCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictLPTSCount.restype = C.c_int
    self.dpl.DPLGetMeasureDictLPTSItem.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictLPTSItem.restype = C.c_double
    self.dpl.DPLGetMeasureDictPDU.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetMeasureDictPDU.restype = C.c_int
    self.dpl.DPLGetNamedDestination.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetNamedDestination.restype = C.c_int
    self.dpl.DPLGetNeedAppearances.argtypes = [C.c_int]
    self.dpl.DPLGetNeedAppearances.restype = C.c_int
    self.dpl.DPLGetNextOutline.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetNextOutline.restype = C.c_int
    self.dpl.DPLGetObjectCount.argtypes = [C.c_int]
    self.dpl.DPLGetObjectCount.restype = C.c_int
    self.dpl.DPLGetObjectDecodeError.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetObjectDecodeError.restype = C.c_int
    self.dpl.DPLGetObjectToString.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetObjectToString.restype = C.c_void_p
    self.dpl.DPLGetOpenActionDestination.argtypes = [C.c_int]
    self.dpl.DPLGetOpenActionDestination.restype = C.c_int
    self.dpl.DPLGetOpenActionJavaScript.argtypes = [C.c_int]
    self.dpl.DPLGetOpenActionJavaScript.restype = C.c_wchar_p
    self.dpl.DPLGetOptionalContentConfigCount.argtypes = [C.c_int]
    self.dpl.DPLGetOptionalContentConfigCount.restype = C.c_int
    self.dpl.DPLGetOptionalContentConfigLocked.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentConfigLocked.restype = C.c_int
    self.dpl.DPLGetOptionalContentConfigOrderCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentConfigOrderCount.restype = C.c_int
    self.dpl.DPLGetOptionalContentConfigOrderItemID.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentConfigOrderItemID.restype = C.c_int
    self.dpl.DPLGetOptionalContentConfigOrderItemLabel.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentConfigOrderItemLabel.restype = C.c_wchar_p
    self.dpl.DPLGetOptionalContentConfigOrderItemLevel.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentConfigOrderItemLevel.restype = C.c_int
    self.dpl.DPLGetOptionalContentConfigOrderItemType.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentConfigOrderItemType.restype = C.c_int
    self.dpl.DPLGetOptionalContentConfigState.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentConfigState.restype = C.c_int
    self.dpl.DPLGetOptionalContentGroupID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentGroupID.restype = C.c_int
    self.dpl.DPLGetOptionalContentGroupName.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentGroupName.restype = C.c_wchar_p
    self.dpl.DPLGetOptionalContentGroupPrintable.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentGroupPrintable.restype = C.c_int
    self.dpl.DPLGetOptionalContentGroupVisible.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOptionalContentGroupVisible.restype = C.c_int
    self.dpl.DPLGetOrigin.argtypes = [C.c_int]
    self.dpl.DPLGetOrigin.restype = C.c_int
    self.dpl.DPLGetOutlineActionID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlineActionID.restype = C.c_int
    self.dpl.DPLGetOutlineColor.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetOutlineColor.restype = C.c_double
    self.dpl.DPLGetOutlineDest.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlineDest.restype = C.c_int
    self.dpl.DPLGetOutlineID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlineID.restype = C.c_int
    self.dpl.DPLGetOutlineJavaScript.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlineJavaScript.restype = C.c_wchar_p
    self.dpl.DPLGetOutlineObjectNumber.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlineObjectNumber.restype = C.c_int
    self.dpl.DPLGetOutlineOpenFile.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlineOpenFile.restype = C.c_wchar_p
    self.dpl.DPLGetOutlinePage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlinePage.restype = C.c_int
    self.dpl.DPLGetOutlineStyle.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlineStyle.restype = C.c_int
    self.dpl.DPLGetOutlineWebLink.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetOutlineWebLink.restype = C.c_wchar_p
    self.dpl.DPLGetPDF417SymbolHeight.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double]
    self.dpl.DPLGetPDF417SymbolHeight.restype = C.c_double
    self.dpl.DPLGetPDF417SymbolWidth.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double]
    self.dpl.DPLGetPDF417SymbolWidth.restype = C.c_double
    self.dpl.DPLGetPageBox.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetPageBox.restype = C.c_double
    self.dpl.DPLGetPageColorSpaces.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetPageColorSpaces.restype = C.c_wchar_p
    self.dpl.DPLGetPageContentToString.argtypes = [C.c_int]
    self.dpl.DPLGetPageContentToString.restype = C.c_void_p
    self.dpl.DPLGetPageImageList.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetPageImageList.restype = C.c_int
    self.dpl.DPLGetPageJavaScript.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetPageJavaScript.restype = C.c_wchar_p
    self.dpl.DPLGetPageLGIDictContent.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetPageLGIDictContent.restype = C.c_wchar_p
    self.dpl.DPLGetPageLGIDictCount.argtypes = [C.c_int]
    self.dpl.DPLGetPageLGIDictCount.restype = C.c_int
    self.dpl.DPLGetPageLabel.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetPageLabel.restype = C.c_wchar_p
    self.dpl.DPLGetPageLayout.argtypes = [C.c_int]
    self.dpl.DPLGetPageLayout.restype = C.c_int
    self.dpl.DPLGetPageMetricsToString.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetPageMetricsToString.restype = C.c_void_p
    self.dpl.DPLGetPageMode.argtypes = [C.c_int]
    self.dpl.DPLGetPageMode.restype = C.c_int
    self.dpl.DPLGetPageText.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetPageText.restype = C.c_wchar_p
    self.dpl.DPLGetPageUserUnit.argtypes = [C.c_int]
    self.dpl.DPLGetPageUserUnit.restype = C.c_double
    self.dpl.DPLGetPageViewPortCount.argtypes = [C.c_int]
    self.dpl.DPLGetPageViewPortCount.restype = C.c_int
    self.dpl.DPLGetPageViewPortID.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetPageViewPortID.restype = C.c_int
    self.dpl.DPLGetParentOutline.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetParentOutline.restype = C.c_int
    self.dpl.DPLGetPrevOutline.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetPrevOutline.restype = C.c_int
    self.dpl.DPLGetPrintPreviewBitmapToString.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetPrintPreviewBitmapToString.restype = C.c_void_p
    self.dpl.DPLGetPrinterBins.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetPrinterBins.restype = C.c_wchar_p
    self.dpl.DPLGetPrinterDevModeToString.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetPrinterDevModeToString.restype = C.c_void_p
    self.dpl.DPLGetPrinterMediaTypes.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetPrinterMediaTypes.restype = C.c_wchar_p
    self.dpl.DPLGetPrinterNames.argtypes = [C.c_int]
    self.dpl.DPLGetPrinterNames.restype = C.c_wchar_p
    self.dpl.DPLGetRenderScale.argtypes = [C.c_int]
    self.dpl.DPLGetRenderScale.restype = C.c_double
    self.dpl.DPLGetScale.argtypes = [C.c_int]
    self.dpl.DPLGetScale.restype = C.c_double
    self.dpl.DPLGetSignProcessByteRange.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetSignProcessByteRange.restype = C.c_int
    self.dpl.DPLGetSignProcessResult.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetSignProcessResult.restype = C.c_int
    self.dpl.DPLGetStringListCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetStringListCount.restype = C.c_int
    self.dpl.DPLGetStringListItem.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetStringListItem.restype = C.c_wchar_p
    self.dpl.DPLGetTabOrderMode.argtypes = [C.c_int]
    self.dpl.DPLGetTabOrderMode.restype = C.c_wchar_p
    self.dpl.DPLGetTableCellDblProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTableCellDblProperty.restype = C.c_double
    self.dpl.DPLGetTableCellIntProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTableCellIntProperty.restype = C.c_int
    self.dpl.DPLGetTableCellStrProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTableCellStrProperty.restype = C.c_wchar_p
    self.dpl.DPLGetTableColumnCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetTableColumnCount.restype = C.c_int
    self.dpl.DPLGetTableLastDrawnRow.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetTableLastDrawnRow.restype = C.c_int
    self.dpl.DPLGetTableRowCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetTableRowCount.restype = C.c_int
    self.dpl.DPLGetTempPath.argtypes = [C.c_int]
    self.dpl.DPLGetTempPath.restype = C.c_wchar_p
    self.dpl.DPLGetTextAscent.argtypes = [C.c_int]
    self.dpl.DPLGetTextAscent.restype = C.c_double
    self.dpl.DPLGetTextBlockAsString.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockAsString.restype = C.c_wchar_p
    self.dpl.DPLGetTextBlockBound.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockBound.restype = C.c_double
    self.dpl.DPLGetTextBlockCharWidth.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockCharWidth.restype = C.c_double
    self.dpl.DPLGetTextBlockColor.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockColor.restype = C.c_double
    self.dpl.DPLGetTextBlockColorType.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockColorType.restype = C.c_int
    self.dpl.DPLGetTextBlockCount.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockCount.restype = C.c_int
    self.dpl.DPLGetTextBlockFontName.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockFontName.restype = C.c_wchar_p
    self.dpl.DPLGetTextBlockFontSize.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockFontSize.restype = C.c_double
    self.dpl.DPLGetTextBlockText.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetTextBlockText.restype = C.c_wchar_p
    self.dpl.DPLGetTextBound.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetTextBound.restype = C.c_double
    self.dpl.DPLGetTextDescent.argtypes = [C.c_int]
    self.dpl.DPLGetTextDescent.restype = C.c_double
    self.dpl.DPLGetTextHeight.argtypes = [C.c_int]
    self.dpl.DPLGetTextHeight.restype = C.c_double
    self.dpl.DPLGetTextSize.argtypes = [C.c_int]
    self.dpl.DPLGetTextSize.restype = C.c_double
    self.dpl.DPLGetTextWidth.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetTextWidth.restype = C.c_double
    self.dpl.DPLGetUnicodeCharactersFromEncoding.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetUnicodeCharactersFromEncoding.restype = C.c_wchar_p
    self.dpl.DPLGetViewPortBBox.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLGetViewPortBBox.restype = C.c_double
    self.dpl.DPLGetViewPortMeasureDict.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetViewPortMeasureDict.restype = C.c_int
    self.dpl.DPLGetViewPortName.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetViewPortName.restype = C.c_wchar_p
    self.dpl.DPLGetViewPortPtDataDict.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetViewPortPtDataDict.restype = C.c_int
    self.dpl.DPLGetViewerPreferences.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetViewerPreferences.restype = C.c_int
    self.dpl.DPLGetWrappedText.argtypes = [C.c_int, C.c_double, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLGetWrappedText.restype = C.c_wchar_p
    self.dpl.DPLGetWrappedTextBreakString.argtypes = [C.c_int, C.c_double, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLGetWrappedTextBreakString.restype = C.c_wchar_p
    self.dpl.DPLGetWrappedTextHeight.argtypes = [C.c_int, C.c_double, C.c_wchar_p]
    self.dpl.DPLGetWrappedTextHeight.restype = C.c_double
    self.dpl.DPLGetWrappedTextLineCount.argtypes = [C.c_int, C.c_double, C.c_wchar_p]
    self.dpl.DPLGetWrappedTextLineCount.restype = C.c_int
    self.dpl.DPLGetXFAFormFieldCount.argtypes = [C.c_int]
    self.dpl.DPLGetXFAFormFieldCount.restype = C.c_int
    self.dpl.DPLGetXFAFormFieldName.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetXFAFormFieldName.restype = C.c_wchar_p
    self.dpl.DPLGetXFAFormFieldNames.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetXFAFormFieldNames.restype = C.c_wchar_p
    self.dpl.DPLGetXFAFormFieldValue.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLGetXFAFormFieldValue.restype = C.c_wchar_p
    self.dpl.DPLGetXFAToString.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGetXFAToString.restype = C.c_void_p
    self.dpl.DPLGlobalJavaScriptCount.argtypes = [C.c_int]
    self.dpl.DPLGlobalJavaScriptCount.restype = C.c_int
    self.dpl.DPLGlobalJavaScriptPackageName.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLGlobalJavaScriptPackageName.restype = C.c_wchar_p
    self.dpl.DPLHasFontResources.argtypes = [C.c_int]
    self.dpl.DPLHasFontResources.restype = C.c_int
    self.dpl.DPLHasPageBox.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLHasPageBox.restype = C.c_int
    self.dpl.DPLHidePage.argtypes = [C.c_int]
    self.dpl.DPLHidePage.restype = C.c_int
    self.dpl.DPLImageCount.argtypes = [C.c_int]
    self.dpl.DPLImageCount.restype = C.c_int
    self.dpl.DPLImageFillColor.argtypes = [C.c_int]
    self.dpl.DPLImageFillColor.restype = C.c_int
    self.dpl.DPLImageHeight.argtypes = [C.c_int]
    self.dpl.DPLImageHeight.restype = C.c_int
    self.dpl.DPLImageHorizontalResolution.argtypes = [C.c_int]
    self.dpl.DPLImageHorizontalResolution.restype = C.c_int
    self.dpl.DPLImageResolutionUnits.argtypes = [C.c_int]
    self.dpl.DPLImageResolutionUnits.restype = C.c_int
    self.dpl.DPLImageType.argtypes = [C.c_int]
    self.dpl.DPLImageType.restype = C.c_int
    self.dpl.DPLImageVerticalResolution.argtypes = [C.c_int]
    self.dpl.DPLImageVerticalResolution.restype = C.c_int
    self.dpl.DPLImageWidth.argtypes = [C.c_int]
    self.dpl.DPLImageWidth.restype = C.c_int
    self.dpl.DPLImportEMFFromFile.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLImportEMFFromFile.restype = C.c_int
    self.dpl.DPLInsertPages.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLInsertPages.restype = C.c_int
    self.dpl.DPLInsertTableColumns.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLInsertTableColumns.restype = C.c_int
    self.dpl.DPLInsertTableRows.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLInsertTableRows.restype = C.c_int
    self.dpl.DPLIsAnnotFormField.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLIsAnnotFormField.restype = C.c_int
    self.dpl.DPLIsLinearized.argtypes = [C.c_int]
    self.dpl.DPLIsLinearized.restype = C.c_int
    self.dpl.DPLIsTaggedPDF.argtypes = [C.c_int]
    self.dpl.DPLIsTaggedPDF.restype = C.c_int
    self.dpl.DPLLastErrorCode.argtypes = [C.c_int]
    self.dpl.DPLLastErrorCode.restype = C.c_int
    self.dpl.DPLLastRenderError.argtypes = [C.c_int]
    self.dpl.DPLLastRenderError.restype = C.c_wchar_p
    self.dpl.DPLLibraryVersion.argtypes = [C.c_int]
    self.dpl.DPLLibraryVersion.restype = C.c_wchar_p
    self.dpl.DPLLibraryVersionEx.argtypes = [C.c_int]
    self.dpl.DPLLibraryVersionEx.restype = C.c_wchar_p
    self.dpl.DPLLicenseInfo.argtypes = [C.c_int]
    self.dpl.DPLLicenseInfo.restype = C.c_wchar_p
    self.dpl.DPLLinearizeFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLLinearizeFile.restype = C.c_int
    self.dpl.DPLLoadFromCanvasDC.argtypes = [C.c_int, C.c_double, C.c_int]
    self.dpl.DPLLoadFromCanvasDC.restype = C.c_int
    self.dpl.DPLLoadFromFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLLoadFromFile.restype = C.c_int
    self.dpl.DPLLoadFromString.argtypes = [C.c_int, C.c_void_p, C.c_wchar_p]
    self.dpl.DPLLoadFromString.restype = C.c_int
    self.dpl.DPLLoadState.argtypes = [C.c_int]
    self.dpl.DPLLoadState.restype = C.c_int
    self.dpl.DPLMergeDocument.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLMergeDocument.restype = C.c_int
    self.dpl.DPLMergeFileList.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLMergeFileList.restype = C.c_int
    self.dpl.DPLMergeFileListFast.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLMergeFileListFast.restype = C.c_int
    self.dpl.DPLMergeFiles.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLMergeFiles.restype = C.c_int
    self.dpl.DPLMergeTableCells.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLMergeTableCells.restype = C.c_int
    self.dpl.DPLMoveContentStream.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLMoveContentStream.restype = C.c_int
    self.dpl.DPLMoveOutlineAfter.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLMoveOutlineAfter.restype = C.c_int
    self.dpl.DPLMoveOutlineBefore.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLMoveOutlineBefore.restype = C.c_int
    self.dpl.DPLMovePage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLMovePage.restype = C.c_int
    self.dpl.DPLMovePath.argtypes = [C.c_int, C.c_double, C.c_double]
    self.dpl.DPLMovePath.restype = C.c_int
    self.dpl.DPLMultiplyScale.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLMultiplyScale.restype = C.c_int
    self.dpl.DPLNewCMYKAxialShader.argtypes = [C.c_int, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLNewCMYKAxialShader.restype = C.c_int
    self.dpl.DPLNewChildFormField.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLNewChildFormField.restype = C.c_int
    self.dpl.DPLNewContentStream.argtypes = [C.c_int]
    self.dpl.DPLNewContentStream.restype = C.c_int
    self.dpl.DPLNewCustomPrinter.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLNewCustomPrinter.restype = C.c_wchar_p
    self.dpl.DPLNewDestination.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLNewDestination.restype = C.c_int
    self.dpl.DPLNewDocument.argtypes = [C.c_int]
    self.dpl.DPLNewDocument.restype = C.c_int
    self.dpl.DPLNewFormField.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLNewFormField.restype = C.c_int
    self.dpl.DPLNewInternalPrinterObject.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLNewInternalPrinterObject.restype = C.c_int
    self.dpl.DPLNewNamedDestination.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLNewNamedDestination.restype = C.c_int
    self.dpl.DPLNewOptionalContentGroup.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLNewOptionalContentGroup.restype = C.c_int
    self.dpl.DPLNewOutline.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int, C.c_double]
    self.dpl.DPLNewOutline.restype = C.c_int
    self.dpl.DPLNewPage.argtypes = [C.c_int]
    self.dpl.DPLNewPage.restype = C.c_int
    self.dpl.DPLNewPageFromCanvasDC.argtypes = [C.c_int, C.c_double, C.c_int]
    self.dpl.DPLNewPageFromCanvasDC.restype = C.c_int
    self.dpl.DPLNewPages.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLNewPages.restype = C.c_int
    self.dpl.DPLNewPostScriptXObject.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLNewPostScriptXObject.restype = C.c_int
    self.dpl.DPLNewRGBAxialShader.argtypes = [C.c_int, C.c_wchar_p, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLNewRGBAxialShader.restype = C.c_int
    self.dpl.DPLNewSignProcessFromFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLNewSignProcessFromFile.restype = C.c_int
    self.dpl.DPLNewSignProcessFromString.argtypes = [C.c_int, C.c_void_p, C.c_wchar_p]
    self.dpl.DPLNewSignProcessFromString.restype = C.c_int
    self.dpl.DPLNewStaticOutline.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLNewStaticOutline.restype = C.c_int
    self.dpl.DPLNewTilingPatternFromCapturedPage.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLNewTilingPatternFromCapturedPage.restype = C.c_int
    self.dpl.DPLNoEmbedFontListAdd.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLNoEmbedFontListAdd.restype = C.c_int
    self.dpl.DPLNoEmbedFontListCount.argtypes = [C.c_int]
    self.dpl.DPLNoEmbedFontListCount.restype = C.c_int
    self.dpl.DPLNoEmbedFontListGet.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLNoEmbedFontListGet.restype = C.c_wchar_p
    self.dpl.DPLNoEmbedFontListRemoveAll.argtypes = [C.c_int]
    self.dpl.DPLNoEmbedFontListRemoveAll.restype = C.c_int
    self.dpl.DPLNoEmbedFontListRemoveIndex.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLNoEmbedFontListRemoveIndex.restype = C.c_int
    self.dpl.DPLNoEmbedFontListRemoveName.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLNoEmbedFontListRemoveName.restype = C.c_int
    self.dpl.DPLNormalizePage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLNormalizePage.restype = C.c_int
    self.dpl.DPLOpenOutline.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLOpenOutline.restype = C.c_int
    self.dpl.DPLOptionalContentGroupCount.argtypes = [C.c_int]
    self.dpl.DPLOptionalContentGroupCount.restype = C.c_int
    self.dpl.DPLOutlineCount.argtypes = [C.c_int]
    self.dpl.DPLOutlineCount.restype = C.c_int
    self.dpl.DPLOutlineTitle.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLOutlineTitle.restype = C.c_wchar_p
    self.dpl.DPLPDFiumPrintDocument.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLPDFiumPrintDocument.restype = C.c_int
    self.dpl.DPLPageCount.argtypes = [C.c_int]
    self.dpl.DPLPageCount.restype = C.c_int
    self.dpl.DPLPageHasFontResources.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLPageHasFontResources.restype = C.c_int
    self.dpl.DPLPageHeight.argtypes = [C.c_int]
    self.dpl.DPLPageHeight.restype = C.c_double
    self.dpl.DPLPageJavaScriptAction.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLPageJavaScriptAction.restype = C.c_int
    self.dpl.DPLPageRotation.argtypes = [C.c_int]
    self.dpl.DPLPageRotation.restype = C.c_int
    self.dpl.DPLPageWidth.argtypes = [C.c_int]
    self.dpl.DPLPageWidth.restype = C.c_double
    self.dpl.DPLPrintDocument.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLPrintDocument.restype = C.c_int
    self.dpl.DPLPrintDocumentToFile.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLPrintDocumentToFile.restype = C.c_int
    self.dpl.DPLPrintMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLPrintMode.restype = C.c_int
    self.dpl.DPLPrintOptions.argtypes = [C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLPrintOptions.restype = C.c_int
    self.dpl.DPLPrintPages.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLPrintPages.restype = C.c_int
    self.dpl.DPLPrintPagesToFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_wchar_p]
    self.dpl.DPLPrintPagesToFile.restype = C.c_int
    self.dpl.DPLReduceSize.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLReduceSize.restype = C.c_int
    self.dpl.DPLReleaseBuffer.argtypes = [C.c_int, C.c_void_p]
    self.dpl.DPLReleaseBuffer.restype = C.c_int
    self.dpl.DPLReleaseImage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLReleaseImage.restype = C.c_int
    self.dpl.DPLReleaseImageList.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLReleaseImageList.restype = C.c_int
    self.dpl.DPLReleaseLibrary.argtypes = [C.c_int]
    self.dpl.DPLReleaseLibrary.restype = C.c_int
    self.dpl.DPLReleaseSignProcess.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLReleaseSignProcess.restype = C.c_int
    self.dpl.DPLReleaseStringList.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLReleaseStringList.restype = C.c_int
    self.dpl.DPLReleaseTextBlocks.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLReleaseTextBlocks.restype = C.c_int
    self.dpl.DPLRemoveAppearanceStream.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRemoveAppearanceStream.restype = C.c_int
    self.dpl.DPLRemoveCustomInformation.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLRemoveCustomInformation.restype = C.c_int
    self.dpl.DPLRemoveDocument.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRemoveDocument.restype = C.c_int
    self.dpl.DPLRemoveEmbeddedFile.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRemoveEmbeddedFile.restype = C.c_int
    self.dpl.DPLRemoveFormFieldBackgroundColor.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRemoveFormFieldBackgroundColor.restype = C.c_int
    self.dpl.DPLRemoveFormFieldBorderColor.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRemoveFormFieldBorderColor.restype = C.c_int
    self.dpl.DPLRemoveFormFieldChoiceSub.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLRemoveFormFieldChoiceSub.restype = C.c_int
    self.dpl.DPLRemoveGlobalJavaScript.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLRemoveGlobalJavaScript.restype = C.c_int
    self.dpl.DPLRemoveOpenAction.argtypes = [C.c_int]
    self.dpl.DPLRemoveOpenAction.restype = C.c_int
    self.dpl.DPLRemoveOutline.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRemoveOutline.restype = C.c_int
    self.dpl.DPLRemovePageBox.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRemovePageBox.restype = C.c_int
    self.dpl.DPLRemoveSharedContentStreams.argtypes = [C.c_int]
    self.dpl.DPLRemoveSharedContentStreams.restype = C.c_int
    self.dpl.DPLRemoveStyle.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLRemoveStyle.restype = C.c_int
    self.dpl.DPLRemoveUsageRights.argtypes = [C.c_int]
    self.dpl.DPLRemoveUsageRights.restype = C.c_int
    self.dpl.DPLRemoveXFAEntries.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRemoveXFAEntries.restype = C.c_int
    self.dpl.DPLRenderAsMultipageTIFFToFile.argtypes = [C.c_int, C.c_double, C.c_wchar_p, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLRenderAsMultipageTIFFToFile.restype = C.c_int
    self.dpl.DPLRenderDocumentToFile.argtypes = [C.c_int, C.c_double, C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLRenderDocumentToFile.restype = C.c_int
    self.dpl.DPLRenderPageToDC.argtypes = [C.c_int, C.c_double, C.c_int, ]
    self.dpl.DPLRenderPageToDC.restype = C.c_int
    self.dpl.DPLRenderPageToFile.argtypes = [C.c_int, C.c_double, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLRenderPageToFile.restype = C.c_int
    self.dpl.DPLRenderPageToString.argtypes = [C.c_int, C.c_double, C.c_int, C.c_int]
    self.dpl.DPLRenderPageToString.restype = C.c_void_p
    self.dpl.DPLReplaceFonts.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLReplaceFonts.restype = C.c_int
    self.dpl.DPLReplaceImage.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLReplaceImage.restype = C.c_int
    self.dpl.DPLReplaceTag.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLReplaceTag.restype = C.c_int
    self.dpl.DPLRequestPrinterStatus.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRequestPrinterStatus.restype = C.c_int
    self.dpl.DPLRetrieveCustomDataToFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLRetrieveCustomDataToFile.restype = C.c_int
    self.dpl.DPLRetrieveCustomDataToString.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLRetrieveCustomDataToString.restype = C.c_void_p
    self.dpl.DPLReverseImage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLReverseImage.restype = C.c_int
    self.dpl.DPLRotatePage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLRotatePage.restype = C.c_int
    self.dpl.DPLSaveFontToFile.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSaveFontToFile.restype = C.c_int
    self.dpl.DPLSaveImageListItemDataToFile.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSaveImageListItemDataToFile.restype = C.c_int
    self.dpl.DPLSaveImageToFile.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSaveImageToFile.restype = C.c_int
    self.dpl.DPLSaveImageToString.argtypes = [C.c_int]
    self.dpl.DPLSaveImageToString.restype = C.c_void_p
    self.dpl.DPLSaveState.argtypes = [C.c_int]
    self.dpl.DPLSaveState.restype = C.c_int
    self.dpl.DPLSaveStyle.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSaveStyle.restype = C.c_int
    self.dpl.DPLSaveToFile.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSaveToFile.restype = C.c_int
    self.dpl.DPLSaveToString.argtypes = [C.c_int]
    self.dpl.DPLSaveToString.restype = C.c_void_p
    self.dpl.DPLSecurityInfo.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSecurityInfo.restype = C.c_int
    self.dpl.DPLSelectContentStream.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSelectContentStream.restype = C.c_int
    self.dpl.DPLSelectDocument.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSelectDocument.restype = C.c_int
    self.dpl.DPLSelectFont.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSelectFont.restype = C.c_int
    self.dpl.DPLSelectImage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSelectImage.restype = C.c_int
    self.dpl.DPLSelectPage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSelectPage.restype = C.c_int
    self.dpl.DPLSelectRenderer.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSelectRenderer.restype = C.c_int
    self.dpl.DPLSelectedDocument.argtypes = [C.c_int]
    self.dpl.DPLSelectedDocument.restype = C.c_int
    self.dpl.DPLSelectedFont.argtypes = [C.c_int]
    self.dpl.DPLSelectedFont.restype = C.c_int
    self.dpl.DPLSelectedImage.argtypes = [C.c_int]
    self.dpl.DPLSelectedImage.restype = C.c_int
    self.dpl.DPLSelectedPage.argtypes = [C.c_int]
    self.dpl.DPLSelectedPage.restype = C.c_int
    self.dpl.DPLSelectedRenderer.argtypes = [C.c_int]
    self.dpl.DPLSelectedRenderer.restype = C.c_int
    self.dpl.DPLSetActionURL.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetActionURL.restype = C.c_int
    self.dpl.DPLSetAnnotBorderColor.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetAnnotBorderColor.restype = C.c_int
    self.dpl.DPLSetAnnotBorderStyle.argtypes = [C.c_int, C.c_int, C.c_double, C.c_int, C.c_double, C.c_double]
    self.dpl.DPLSetAnnotBorderStyle.restype = C.c_int
    self.dpl.DPLSetAnnotContents.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetAnnotContents.restype = C.c_int
    self.dpl.DPLSetAnnotDblProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetAnnotDblProperty.restype = C.c_int
    self.dpl.DPLSetAnnotIntProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetAnnotIntProperty.restype = C.c_int
    self.dpl.DPLSetAnnotOptional.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetAnnotOptional.restype = C.c_int
    self.dpl.DPLSetAnnotQuadPoints.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetAnnotQuadPoints.restype = C.c_int
    self.dpl.DPLSetAnnotRect.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetAnnotRect.restype = C.c_int
    self.dpl.DPLSetAnnotStrProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetAnnotStrProperty.restype = C.c_int
    self.dpl.DPLSetAnsiMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetAnsiMode.restype = C.c_int
    self.dpl.DPLSetAppendInputFromString.argtypes = [C.c_int, C.c_void_p]
    self.dpl.DPLSetAppendInputFromString.restype = C.c_int
    self.dpl.DPLSetBaseURL.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetBaseURL.restype = C.c_int
    self.dpl.DPLSetBlendMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetBlendMode.restype = C.c_int
    self.dpl.DPLSetBreakString.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetBreakString.restype = C.c_int
    self.dpl.DPLSetCSDictEPSG.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetCSDictEPSG.restype = C.c_int
    self.dpl.DPLSetCSDictType.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetCSDictType.restype = C.c_int
    self.dpl.DPLSetCSDictWKT.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetCSDictWKT.restype = C.c_int
    self.dpl.DPLSetCairoFileName.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetCairoFileName.restype = C.c_int
    self.dpl.DPLSetCapturedPageOptional.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetCapturedPageOptional.restype = C.c_int
    self.dpl.DPLSetCapturedPageTransparencyGroup.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetCapturedPageTransparencyGroup.restype = C.c_int
    self.dpl.DPLSetCatalogInformation.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetCatalogInformation.restype = C.c_int
    self.dpl.DPLSetCharWidth.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetCharWidth.restype = C.c_int
    self.dpl.DPLSetClippingPath.argtypes = [C.c_int]
    self.dpl.DPLSetClippingPath.restype = C.c_int
    self.dpl.DPLSetClippingPathEvenOdd.argtypes = [C.c_int]
    self.dpl.DPLSetClippingPathEvenOdd.restype = C.c_int
    self.dpl.DPLSetCompatibility.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetCompatibility.restype = C.c_int
    self.dpl.DPLSetContentStreamFromString.argtypes = [C.c_int, C.c_void_p]
    self.dpl.DPLSetContentStreamFromString.restype = C.c_int
    self.dpl.DPLSetContentStreamOptional.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetContentStreamOptional.restype = C.c_int
    self.dpl.DPLSetCropBox.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetCropBox.restype = C.c_int
    self.dpl.DPLSetCustomInformation.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetCustomInformation.restype = C.c_int
    self.dpl.DPLSetCustomLineDash.argtypes = [C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetCustomLineDash.restype = C.c_int
    self.dpl.DPLSetDPLRFileName.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetDPLRFileName.restype = C.c_int
    self.dpl.DPLSetDecodeMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetDecodeMode.restype = C.c_int
    self.dpl.DPLSetDestProperties.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetDestProperties.restype = C.c_int
    self.dpl.DPLSetDestValue.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetDestValue.restype = C.c_int
    self.dpl.DPLSetDocumentMetadata.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetDocumentMetadata.restype = C.c_int
    self.dpl.DPLSetEmbeddedFileStrProperty.argtypes = [C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetEmbeddedFileStrProperty.restype = C.c_int
    self.dpl.DPLSetFillColor.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFillColor.restype = C.c_int
    self.dpl.DPLSetFillColorCMYK.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFillColorCMYK.restype = C.c_int
    self.dpl.DPLSetFillColorSep.argtypes = [C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetFillColorSep.restype = C.c_int
    self.dpl.DPLSetFillShader.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFillShader.restype = C.c_int
    self.dpl.DPLSetFillTilingPattern.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFillTilingPattern.restype = C.c_int
    self.dpl.DPLSetFindImagesMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetFindImagesMode.restype = C.c_int
    self.dpl.DPLSetFontEncoding.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetFontEncoding.restype = C.c_int
    self.dpl.DPLSetFontFlags.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFontFlags.restype = C.c_int
    self.dpl.DPLSetFormFieldAlignment.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldAlignment.restype = C.c_int
    self.dpl.DPLSetFormFieldAnnotFlags.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldAnnotFlags.restype = C.c_int
    self.dpl.DPLSetFormFieldAppearanceFromString.argtypes = [C.c_int, C.c_int, C.c_void_p, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldAppearanceFromString.restype = C.c_int
    self.dpl.DPLSetFormFieldBackgroundColor.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldBackgroundColor.restype = C.c_int
    self.dpl.DPLSetFormFieldBackgroundColorCMYK.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldBackgroundColorCMYK.restype = C.c_int
    self.dpl.DPLSetFormFieldBackgroundColorGray.argtypes = [C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetFormFieldBackgroundColorGray.restype = C.c_int
    self.dpl.DPLSetFormFieldBackgroundColorSep.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetFormFieldBackgroundColorSep.restype = C.c_int
    self.dpl.DPLSetFormFieldBorderColor.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldBorderColor.restype = C.c_int
    self.dpl.DPLSetFormFieldBorderColorCMYK.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldBorderColorCMYK.restype = C.c_int
    self.dpl.DPLSetFormFieldBorderColorGray.argtypes = [C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetFormFieldBorderColorGray.restype = C.c_int
    self.dpl.DPLSetFormFieldBorderColorSep.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetFormFieldBorderColorSep.restype = C.c_int
    self.dpl.DPLSetFormFieldBorderStyle.argtypes = [C.c_int, C.c_int, C.c_double, C.c_int, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldBorderStyle.restype = C.c_int
    self.dpl.DPLSetFormFieldBounds.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldBounds.restype = C.c_int
    self.dpl.DPLSetFormFieldCalcOrder.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldCalcOrder.restype = C.c_int
    self.dpl.DPLSetFormFieldCaption.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldCaption.restype = C.c_int
    self.dpl.DPLSetFormFieldCheckStyle.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldCheckStyle.restype = C.c_int
    self.dpl.DPLSetFormFieldCheckboxColor.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldCheckboxColor.restype = C.c_int
    self.dpl.DPLSetFormFieldChildTitle.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldChildTitle.restype = C.c_int
    self.dpl.DPLSetFormFieldChoiceSub.argtypes = [C.c_int, C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetFormFieldChoiceSub.restype = C.c_int
    self.dpl.DPLSetFormFieldChoiceType.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldChoiceType.restype = C.c_int
    self.dpl.DPLSetFormFieldColor.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldColor.restype = C.c_int
    self.dpl.DPLSetFormFieldColorCMYK.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetFormFieldColorCMYK.restype = C.c_int
    self.dpl.DPLSetFormFieldColorSep.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetFormFieldColorSep.restype = C.c_int
    self.dpl.DPLSetFormFieldComb.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldComb.restype = C.c_int
    self.dpl.DPLSetFormFieldCustomDict.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldCustomDict.restype = C.c_int
    self.dpl.DPLSetFormFieldDefaultValue.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldDefaultValue.restype = C.c_int
    self.dpl.DPLSetFormFieldDefaultValueEx.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetFormFieldDefaultValueEx.restype = C.c_int
    self.dpl.DPLSetFormFieldDescription.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldDescription.restype = C.c_int
    self.dpl.DPLSetFormFieldFlags.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldFlags.restype = C.c_int
    self.dpl.DPLSetFormFieldFont.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldFont.restype = C.c_int
    self.dpl.DPLSetFormFieldFormatMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldFormatMode.restype = C.c_int
    self.dpl.DPLSetFormFieldHighlightMode.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldHighlightMode.restype = C.c_int
    self.dpl.DPLSetFormFieldIcon.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldIcon.restype = C.c_int
    self.dpl.DPLSetFormFieldIconStyle.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldIconStyle.restype = C.c_int
    self.dpl.DPLSetFormFieldLockAction.argtypes = [C.c_int, C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetFormFieldLockAction.restype = C.c_int
    self.dpl.DPLSetFormFieldMaxLen.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldMaxLen.restype = C.c_int
    self.dpl.DPLSetFormFieldMetadata.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldMetadata.restype = C.c_int
    self.dpl.DPLSetFormFieldNoExport.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldNoExport.restype = C.c_int
    self.dpl.DPLSetFormFieldOptional.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldOptional.restype = C.c_int
    self.dpl.DPLSetFormFieldPage.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldPage.restype = C.c_int
    self.dpl.DPLSetFormFieldPrintable.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldPrintable.restype = C.c_int
    self.dpl.DPLSetFormFieldReadOnly.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldReadOnly.restype = C.c_int
    self.dpl.DPLSetFormFieldRequired.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldRequired.restype = C.c_int
    self.dpl.DPLSetFormFieldResetAction.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldResetAction.restype = C.c_int
    self.dpl.DPLSetFormFieldRichTextString.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetFormFieldRichTextString.restype = C.c_int
    self.dpl.DPLSetFormFieldRotation.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldRotation.restype = C.c_int
    self.dpl.DPLSetFormFieldSignatureImage.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldSignatureImage.restype = C.c_int
    self.dpl.DPLSetFormFieldStandardFont.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldStandardFont.restype = C.c_int
    self.dpl.DPLSetFormFieldSubmitAction.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetFormFieldSubmitAction.restype = C.c_int
    self.dpl.DPLSetFormFieldSubmitActionEx.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetFormFieldSubmitActionEx.restype = C.c_int
    self.dpl.DPLSetFormFieldTabOrder.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldTabOrder.restype = C.c_int
    self.dpl.DPLSetFormFieldTextFlags.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldTextFlags.restype = C.c_int
    self.dpl.DPLSetFormFieldTextSize.argtypes = [C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetFormFieldTextSize.restype = C.c_int
    self.dpl.DPLSetFormFieldTitle.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldTitle.restype = C.c_int
    self.dpl.DPLSetFormFieldValue.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetFormFieldValue.restype = C.c_int
    self.dpl.DPLSetFormFieldValueByTitle.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetFormFieldValueByTitle.restype = C.c_int
    self.dpl.DPLSetFormFieldValueEx.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetFormFieldValueEx.restype = C.c_int
    self.dpl.DPLSetFormFieldVisible.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetFormFieldVisible.restype = C.c_int
    self.dpl.DPLSetGDIPlusFileName.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetGDIPlusFileName.restype = C.c_int
    self.dpl.DPLSetGDIPlusOptions.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetGDIPlusOptions.restype = C.c_int
    self.dpl.DPLSetHTMLBoldFont.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetHTMLBoldFont.restype = C.c_int
    self.dpl.DPLSetHTMLBoldItalicFont.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetHTMLBoldItalicFont.restype = C.c_int
    self.dpl.DPLSetHTMLItalicFont.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetHTMLItalicFont.restype = C.c_int
    self.dpl.DPLSetHTMLNormalFont.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetHTMLNormalFont.restype = C.c_int
    self.dpl.DPLSetHeaderCommentsFromString.argtypes = [C.c_int, C.c_void_p]
    self.dpl.DPLSetHeaderCommentsFromString.restype = C.c_int
    self.dpl.DPLSetImageAsMask.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetImageAsMask.restype = C.c_int
    self.dpl.DPLSetImageMask.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetImageMask.restype = C.c_int
    self.dpl.DPLSetImageMaskCMYK.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetImageMaskCMYK.restype = C.c_int
    self.dpl.DPLSetImageMaskFromImage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetImageMaskFromImage.restype = C.c_int
    self.dpl.DPLSetImageOptional.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetImageOptional.restype = C.c_int
    self.dpl.DPLSetImageResolution.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetImageResolution.restype = C.c_int
    self.dpl.DPLSetInformation.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetInformation.restype = C.c_int
    self.dpl.DPLSetJPEGQuality.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetJPEGQuality.restype = C.c_int
    self.dpl.DPLSetJavaScriptMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetJavaScriptMode.restype = C.c_int
    self.dpl.DPLSetKerning.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetKerning.restype = C.c_int
    self.dpl.DPLSetLineCap.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetLineCap.restype = C.c_int
    self.dpl.DPLSetLineColor.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetLineColor.restype = C.c_int
    self.dpl.DPLSetLineColorCMYK.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetLineColorCMYK.restype = C.c_int
    self.dpl.DPLSetLineColorSep.argtypes = [C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetLineColorSep.restype = C.c_int
    self.dpl.DPLSetLineDash.argtypes = [C.c_int, C.c_double, C.c_double]
    self.dpl.DPLSetLineDash.restype = C.c_int
    self.dpl.DPLSetLineDashEx.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetLineDashEx.restype = C.c_int
    self.dpl.DPLSetLineJoin.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetLineJoin.restype = C.c_int
    self.dpl.DPLSetLineShader.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetLineShader.restype = C.c_int
    self.dpl.DPLSetLineWidth.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetLineWidth.restype = C.c_int
    self.dpl.DPLSetMarkupAnnotStyle.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetMarkupAnnotStyle.restype = C.c_int
    self.dpl.DPLSetMeasureDictBoundsCount.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetMeasureDictBoundsCount.restype = C.c_int
    self.dpl.DPLSetMeasureDictBoundsItem.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetMeasureDictBoundsItem.restype = C.c_int
    self.dpl.DPLSetMeasureDictCoordinateSystem.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetMeasureDictCoordinateSystem.restype = C.c_int
    self.dpl.DPLSetMeasureDictGPTSCount.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetMeasureDictGPTSCount.restype = C.c_int
    self.dpl.DPLSetMeasureDictGPTSItem.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetMeasureDictGPTSItem.restype = C.c_int
    self.dpl.DPLSetMeasureDictLPTSCount.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetMeasureDictLPTSCount.restype = C.c_int
    self.dpl.DPLSetMeasureDictLPTSItem.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetMeasureDictLPTSItem.restype = C.c_int
    self.dpl.DPLSetMeasureDictPDU.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetMeasureDictPDU.restype = C.c_int
    self.dpl.DPLSetMeasurementUnits.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetMeasurementUnits.restype = C.c_int
    self.dpl.DPLSetMetafileMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetMetafileMode.restype = C.c_int
    self.dpl.DPLSetNeedAppearances.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetNeedAppearances.restype = C.c_int
    self.dpl.DPLSetObjectAsStreamFromString.argtypes = [C.c_int, C.c_int, C.c_void_p, C.c_int]
    self.dpl.DPLSetObjectAsStreamFromString.restype = C.c_int
    self.dpl.DPLSetObjectFromString.argtypes = [C.c_int, C.c_int, C.c_void_p]
    self.dpl.DPLSetObjectFromString.restype = C.c_int
    self.dpl.DPLSetOpenActionDestination.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetOpenActionDestination.restype = C.c_int
    self.dpl.DPLSetOpenActionDestinationFull.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetOpenActionDestinationFull.restype = C.c_int
    self.dpl.DPLSetOpenActionJavaScript.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetOpenActionJavaScript.restype = C.c_int
    self.dpl.DPLSetOpenActionMenu.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetOpenActionMenu.restype = C.c_int
    self.dpl.DPLSetOptionalContentConfigLocked.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetOptionalContentConfigLocked.restype = C.c_int
    self.dpl.DPLSetOptionalContentConfigState.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetOptionalContentConfigState.restype = C.c_int
    self.dpl.DPLSetOptionalContentGroupName.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetOptionalContentGroupName.restype = C.c_int
    self.dpl.DPLSetOptionalContentGroupPrintable.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetOptionalContentGroupPrintable.restype = C.c_int
    self.dpl.DPLSetOptionalContentGroupVisible.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetOptionalContentGroupVisible.restype = C.c_int
    self.dpl.DPLSetOrigin.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetOrigin.restype = C.c_int
    self.dpl.DPLSetOutlineColor.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetOutlineColor.restype = C.c_int
    self.dpl.DPLSetOutlineDestination.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetOutlineDestination.restype = C.c_int
    self.dpl.DPLSetOutlineDestinationFull.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetOutlineDestinationFull.restype = C.c_int
    self.dpl.DPLSetOutlineDestinationZoom.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, C.c_int]
    self.dpl.DPLSetOutlineDestinationZoom.restype = C.c_int
    self.dpl.DPLSetOutlineJavaScript.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetOutlineJavaScript.restype = C.c_int
    self.dpl.DPLSetOutlineNamedDestination.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetOutlineNamedDestination.restype = C.c_int
    self.dpl.DPLSetOutlineOpenFile.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetOutlineOpenFile.restype = C.c_int
    self.dpl.DPLSetOutlineRemoteDestination.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double, C.c_int]
    self.dpl.DPLSetOutlineRemoteDestination.restype = C.c_int
    self.dpl.DPLSetOutlineStyle.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetOutlineStyle.restype = C.c_int
    self.dpl.DPLSetOutlineTitle.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetOutlineTitle.restype = C.c_int
    self.dpl.DPLSetOutlineWebLink.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetOutlineWebLink.restype = C.c_int
    self.dpl.DPLSetOverprint.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetOverprint.restype = C.c_int
    self.dpl.DPLSetPDFAMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetPDFAMode.restype = C.c_int
    self.dpl.DPLSetPDFiumFileName.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetPDFiumFileName.restype = C.c_int
    self.dpl.DPLSetPNGTransparencyColor.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetPNGTransparencyColor.restype = C.c_int
    self.dpl.DPLSetPageActionMenu.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetPageActionMenu.restype = C.c_int
    self.dpl.DPLSetPageBox.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetPageBox.restype = C.c_int
    self.dpl.DPLSetPageContentFromString.argtypes = [C.c_int, C.c_void_p]
    self.dpl.DPLSetPageContentFromString.restype = C.c_int
    self.dpl.DPLSetPageDimensions.argtypes = [C.c_int, C.c_double, C.c_double]
    self.dpl.DPLSetPageDimensions.restype = C.c_int
    self.dpl.DPLSetPageLayout.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetPageLayout.restype = C.c_int
    self.dpl.DPLSetPageMetadata.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetPageMetadata.restype = C.c_int
    self.dpl.DPLSetPageMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetPageMode.restype = C.c_int
    self.dpl.DPLSetPageSize.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetPageSize.restype = C.c_int
    self.dpl.DPLSetPageThumbnail.argtypes = [C.c_int]
    self.dpl.DPLSetPageThumbnail.restype = C.c_int
    self.dpl.DPLSetPageTransparencyGroup.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetPageTransparencyGroup.restype = C.c_int
    self.dpl.DPLSetPageUserUnit.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetPageUserUnit.restype = C.c_int
    self.dpl.DPLSetPrecision.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetPrecision.restype = C.c_int
    self.dpl.DPLSetPrinterDevModeFromString.argtypes = [C.c_int, C.c_void_p]
    self.dpl.DPLSetPrinterDevModeFromString.restype = C.c_int
    self.dpl.DPLSetRenderArea.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetRenderArea.restype = C.c_int
    self.dpl.DPLSetRenderCropType.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetRenderCropType.restype = C.c_int
    self.dpl.DPLSetRenderDCErasePage.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetRenderDCErasePage.restype = C.c_int
    self.dpl.DPLSetRenderDCOffset.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetRenderDCOffset.restype = C.c_int
    self.dpl.DPLSetRenderOptions.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetRenderOptions.restype = C.c_int
    self.dpl.DPLSetRenderScale.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetRenderScale.restype = C.c_int
    self.dpl.DPLSetScale.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetScale.restype = C.c_int
    self.dpl.DPLSetSignProcessAppearanceFromString.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_void_p]
    self.dpl.DPLSetSignProcessAppearanceFromString.restype = C.c_int
    self.dpl.DPLSetSignProcessCertFromStore.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetSignProcessCertFromStore.restype = C.c_int
    self.dpl.DPLSetSignProcessCustomDict.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetSignProcessCustomDict.restype = C.c_int
    self.dpl.DPLSetSignProcessCustomSubFilter.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetSignProcessCustomSubFilter.restype = C.c_int
    self.dpl.DPLSetSignProcessField.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetSignProcessField.restype = C.c_int
    self.dpl.DPLSetSignProcessFieldBounds.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetSignProcessFieldBounds.restype = C.c_int
    self.dpl.DPLSetSignProcessFieldImageFromFile.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetSignProcessFieldImageFromFile.restype = C.c_int
    self.dpl.DPLSetSignProcessFieldImageFromString.argtypes = [C.c_int, C.c_int, C.c_void_p, C.c_int]
    self.dpl.DPLSetSignProcessFieldImageFromString.restype = C.c_int
    self.dpl.DPLSetSignProcessFieldLocked.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetSignProcessFieldLocked.restype = C.c_int
    self.dpl.DPLSetSignProcessFieldMetadata.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetSignProcessFieldMetadata.restype = C.c_int
    self.dpl.DPLSetSignProcessFieldPage.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetSignProcessFieldPage.restype = C.c_int
    self.dpl.DPLSetSignProcessImageLayer.argtypes = [C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetSignProcessImageLayer.restype = C.c_int
    self.dpl.DPLSetSignProcessInfo.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetSignProcessInfo.restype = C.c_int
    self.dpl.DPLSetSignProcessKeyset.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetSignProcessKeyset.restype = C.c_int
    self.dpl.DPLSetSignProcessOptions.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetSignProcessOptions.restype = C.c_int
    self.dpl.DPLSetSignProcessPFXFromFile.argtypes = [C.c_int, C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetSignProcessPFXFromFile.restype = C.c_int
    self.dpl.DPLSetSignProcessPFXFromString.argtypes = [C.c_int, C.c_int, C.c_void_p, C.c_wchar_p]
    self.dpl.DPLSetSignProcessPFXFromString.restype = C.c_int
    self.dpl.DPLSetSignProcessPassthrough.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetSignProcessPassthrough.restype = C.c_int
    self.dpl.DPLSetSignProcessSubFilter.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetSignProcessSubFilter.restype = C.c_int
    self.dpl.DPLSetTabOrderMode.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetTabOrderMode.restype = C.c_int
    self.dpl.DPLSetTableBorderColor.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableBorderColor.restype = C.c_int
    self.dpl.DPLSetTableBorderColorCMYK.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableBorderColorCMYK.restype = C.c_int
    self.dpl.DPLSetTableBorderWidth.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetTableBorderWidth.restype = C.c_int
    self.dpl.DPLSetTableCellAlignment.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetTableCellAlignment.restype = C.c_int
    self.dpl.DPLSetTableCellBackgroundColor.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableCellBackgroundColor.restype = C.c_int
    self.dpl.DPLSetTableCellBackgroundColorCMYK.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableCellBackgroundColorCMYK.restype = C.c_int
    self.dpl.DPLSetTableCellBorderColor.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableCellBorderColor.restype = C.c_int
    self.dpl.DPLSetTableCellBorderColorCMYK.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableCellBorderColorCMYK.restype = C.c_int
    self.dpl.DPLSetTableCellBorderWidth.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetTableCellBorderWidth.restype = C.c_int
    self.dpl.DPLSetTableCellContent.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_wchar_p]
    self.dpl.DPLSetTableCellContent.restype = C.c_int
    self.dpl.DPLSetTableCellPadding.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetTableCellPadding.restype = C.c_int
    self.dpl.DPLSetTableCellTextColor.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableCellTextColor.restype = C.c_int
    self.dpl.DPLSetTableCellTextColorCMYK.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableCellTextColorCMYK.restype = C.c_int
    self.dpl.DPLSetTableCellTextSize.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetTableCellTextSize.restype = C.c_int
    self.dpl.DPLSetTableColumnWidth.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetTableColumnWidth.restype = C.c_int
    self.dpl.DPLSetTableRowHeight.argtypes = [C.c_int, C.c_int, C.c_int, C.c_int, C.c_double]
    self.dpl.DPLSetTableRowHeight.restype = C.c_int
    self.dpl.DPLSetTableThinBorders.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableThinBorders.restype = C.c_int
    self.dpl.DPLSetTableThinBordersCMYK.argtypes = [C.c_int, C.c_int, C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTableThinBordersCMYK.restype = C.c_int
    self.dpl.DPLSetTempFile.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetTempFile.restype = C.c_int
    self.dpl.DPLSetTempPath.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetTempPath.restype = C.c_int
    self.dpl.DPLSetTextAlign.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetTextAlign.restype = C.c_int
    self.dpl.DPLSetTextCharSpacing.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextCharSpacing.restype = C.c_int
    self.dpl.DPLSetTextColor.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTextColor.restype = C.c_int
    self.dpl.DPLSetTextColorCMYK.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTextColorCMYK.restype = C.c_int
    self.dpl.DPLSetTextColorSep.argtypes = [C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetTextColorSep.restype = C.c_int
    self.dpl.DPLSetTextExtractionArea.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTextExtractionArea.restype = C.c_int
    self.dpl.DPLSetTextExtractionOptions.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetTextExtractionOptions.restype = C.c_int
    self.dpl.DPLSetTextExtractionScaling.argtypes = [C.c_int, C.c_int, C.c_double, C.c_double]
    self.dpl.DPLSetTextExtractionScaling.restype = C.c_int
    self.dpl.DPLSetTextExtractionWordGap.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextExtractionWordGap.restype = C.c_int
    self.dpl.DPLSetTextHighlight.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetTextHighlight.restype = C.c_int
    self.dpl.DPLSetTextHighlightColor.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTextHighlightColor.restype = C.c_int
    self.dpl.DPLSetTextHighlightColorCMYK.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTextHighlightColorCMYK.restype = C.c_int
    self.dpl.DPLSetTextHighlightColorSep.argtypes = [C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetTextHighlightColorSep.restype = C.c_int
    self.dpl.DPLSetTextMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetTextMode.restype = C.c_int
    self.dpl.DPLSetTextRise.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextRise.restype = C.c_int
    self.dpl.DPLSetTextScaling.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextScaling.restype = C.c_int
    self.dpl.DPLSetTextShader.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLSetTextShader.restype = C.c_int
    self.dpl.DPLSetTextSize.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextSize.restype = C.c_int
    self.dpl.DPLSetTextSpacing.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextSpacing.restype = C.c_int
    self.dpl.DPLSetTextUnderline.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetTextUnderline.restype = C.c_int
    self.dpl.DPLSetTextUnderlineColor.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTextUnderlineColor.restype = C.c_int
    self.dpl.DPLSetTextUnderlineColorCMYK.argtypes = [C.c_int, C.c_double, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetTextUnderlineColorCMYK.restype = C.c_int
    self.dpl.DPLSetTextUnderlineColorSep.argtypes = [C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetTextUnderlineColorSep.restype = C.c_int
    self.dpl.DPLSetTextUnderlineCustomDash.argtypes = [C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetTextUnderlineCustomDash.restype = C.c_int
    self.dpl.DPLSetTextUnderlineDash.argtypes = [C.c_int, C.c_double, C.c_double]
    self.dpl.DPLSetTextUnderlineDash.restype = C.c_int
    self.dpl.DPLSetTextUnderlineDistance.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextUnderlineDistance.restype = C.c_int
    self.dpl.DPLSetTextUnderlineWidth.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextUnderlineWidth.restype = C.c_int
    self.dpl.DPLSetTextWordSpacing.argtypes = [C.c_int, C.c_double]
    self.dpl.DPLSetTextWordSpacing.restype = C.c_int
    self.dpl.DPLSetTransparency.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetTransparency.restype = C.c_int
    self.dpl.DPLSetUpdateMode.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSetUpdateMode.restype = C.c_int
    self.dpl.DPLSetViewerPreferences.argtypes = [C.c_int, C.c_int, C.c_int]
    self.dpl.DPLSetViewerPreferences.restype = C.c_int
    self.dpl.DPLSetXFAFormFieldAccess.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetXFAFormFieldAccess.restype = C.c_int
    self.dpl.DPLSetXFAFormFieldBorderColor.argtypes = [C.c_int, C.c_wchar_p, C.c_double, C.c_double, C.c_double]
    self.dpl.DPLSetXFAFormFieldBorderColor.restype = C.c_int
    self.dpl.DPLSetXFAFormFieldBorderPresence.argtypes = [C.c_int, C.c_wchar_p, C.c_int]
    self.dpl.DPLSetXFAFormFieldBorderPresence.restype = C.c_int
    self.dpl.DPLSetXFAFormFieldBorderWidth.argtypes = [C.c_int, C.c_wchar_p, C.c_double]
    self.dpl.DPLSetXFAFormFieldBorderWidth.restype = C.c_int
    self.dpl.DPLSetXFAFormFieldValue.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSetXFAFormFieldValue.restype = C.c_int
    self.dpl.DPLSetXFAFromString.argtypes = [C.c_int, C.c_void_p, C.c_int]
    self.dpl.DPLSetXFAFromString.restype = C.c_int
    self.dpl.DPLSetupCustomPrinter.argtypes = [C.c_int, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLSetupCustomPrinter.restype = C.c_int
    self.dpl.DPLSignFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p]
    self.dpl.DPLSignFile.restype = C.c_int
    self.dpl.DPLSplitPageText.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLSplitPageText.restype = C.c_int
    self.dpl.DPLStartPath.argtypes = [C.c_int, C.c_double, C.c_double]
    self.dpl.DPLStartPath.restype = C.c_int
    self.dpl.DPLStoreCustomDataFromFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLStoreCustomDataFromFile.restype = C.c_int
    self.dpl.DPLStoreCustomDataFromString.argtypes = [C.c_int, C.c_wchar_p, C.c_void_p, C.c_int, C.c_int]
    self.dpl.DPLStoreCustomDataFromString.restype = C.c_int
    self.dpl.DPLTestTempPath.argtypes = [C.c_int]
    self.dpl.DPLTestTempPath.restype = C.c_int
    self.dpl.DPLTransformFile.argtypes = [C.c_int, C.c_wchar_p, C.c_wchar_p, C.c_wchar_p, C.c_int, C.c_int]
    self.dpl.DPLTransformFile.restype = C.c_int
    self.dpl.DPLUnlockKey.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLUnlockKey.restype = C.c_int
    self.dpl.DPLUnlocked.argtypes = [C.c_int]
    self.dpl.DPLUnlocked.restype = C.c_int
    self.dpl.DPLUpdateAndFlattenFormField.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLUpdateAndFlattenFormField.restype = C.c_int
    self.dpl.DPLUpdateAppearanceStream.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLUpdateAppearanceStream.restype = C.c_int
    self.dpl.DPLUpdateTrueTypeSubsettedFont.argtypes = [C.c_int, C.c_wchar_p]
    self.dpl.DPLUpdateTrueTypeSubsettedFont.restype = C.c_int
    self.dpl.DPLUseKerning.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLUseKerning.restype = C.c_int
    self.dpl.DPLUseUnsafeContentStreams.argtypes = [C.c_int, C.c_int]
    self.dpl.DPLUseUnsafeContentStreams.restype = C.c_int

    # Create an instance of the library
    self.instanceID = self.dpl.DPLCreateLibrary()

  # Send binary data to QPL
  def StringParm(self, ba):
    if 0 in ba:
      bufferLen = len(ba)
      a = self.dpl.DPLCreateBuffer(self.instanceID, bufferLen)
      baType = C.c_char * bufferLen
      baPtr = baType.from_buffer(ba)
      self.dpl.DPLAddToBuffer(self.instanceID, a, C.addressof(baPtr), bufferLen)
      return a, True
    else:
      a = (C.c_char * len(ba)).from_buffer(ba)
      return a, False

  def AddArcToPath(self, CenterX, CenterY, TotalAngle):
    result = self.dpl.DPLAddArcToPath(self.instanceID, CenterX, CenterY, TotalAngle)
    return result

  def AddBoxToPath(self, Left, Top, Width, Height):
    result = self.dpl.DPLAddBoxToPath(self.instanceID, Left, Top, Width, Height)
    return result

  def AddCJKFont(self, CJKFontID):
    result = self.dpl.DPLAddCJKFont(self.instanceID, CJKFontID)
    return result

  def AddCurveToPath(self, CtAX, CtAY, CtBX, CtBY, EndX, EndY):
    result = self.dpl.DPLAddCurveToPath(self.instanceID, CtAX, CtAY, CtBX, CtBY, EndX, EndY)
    return result

  def AddEmbeddedFile(self, FileName, MIMEType):
    result = self.dpl.DPLAddEmbeddedFile(self.instanceID, FileName, MIMEType)
    return result

  def AddFileAttachment(self, Title, EmbeddedFileID):
    result = self.dpl.DPLAddFileAttachment(self.instanceID, Title, EmbeddedFileID)
    return result

  def AddFormFieldChoiceSub(self, Index, SubName, DisplayName):
    result = self.dpl.DPLAddFormFieldChoiceSub(self.instanceID, Index, SubName, DisplayName)
    return result

  def AddFormFieldSub(self, Index, SubName):
    result = self.dpl.DPLAddFormFieldSub(self.instanceID, Index, SubName)
    return result

  def AddFormFieldSubEx(self, Index, SubName, Options):
    result = self.dpl.DPLAddFormFieldSubEx(self.instanceID, Index, SubName, Options)
    return result

  def AddFormFont(self, FontID):
    result = self.dpl.DPLAddFormFont(self.instanceID, FontID)
    return result

  def AddFreeTextAnnotation(self, Left, Top, Width, Height, Text, Angle, Options):
    result = self.dpl.DPLAddFreeTextAnnotation(self.instanceID, Left, Top, Width, Height, Text, Angle, Options)
    return result

  def AddFreeTextAnnotationEx(self, Left, Top, Width, Height, Text, Angle, Options, Transparency):
    result = self.dpl.DPLAddFreeTextAnnotationEx(self.instanceID, Left, Top, Width, Height, Text, Angle, Options, Transparency)
    return result

  def AddGlobalJavaScript(self, PackageName, JavaScript):
    result = self.dpl.DPLAddGlobalJavaScript(self.instanceID, PackageName, JavaScript)
    return result

  def AddImageFromFile(self, FileName, Options):
    result = self.dpl.DPLAddImageFromFile(self.instanceID, FileName, Options)
    return result

  def AddImageFromFileOffset(self, FileName, Offset, DataLength, Options):
    result = self.dpl.DPLAddImageFromFileOffset(self.instanceID, FileName, Offset, DataLength, Options)
    return result

  def AddImageFromString(self, Source, Options):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLAddImageFromString(self.instanceID, SourceBuffer, Options)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def AddLGIDictToPage(self, DictContent):
    result = self.dpl.DPLAddLGIDictToPage(self.instanceID, DictContent)
    return result

  def AddLineToPath(self, EndX, EndY):
    result = self.dpl.DPLAddLineToPath(self.instanceID, EndX, EndY)
    return result

  def AddLinkToDestination(self, Left, Top, Width, Height, DestID, Options):
    result = self.dpl.DPLAddLinkToDestination(self.instanceID, Left, Top, Width, Height, DestID, Options)
    return result

  def AddLinkToEmbeddedFile(self, Left, Top, Width, Height, EmbeddedFileID, Title, Contents, IconType, Transpareny):
    result = self.dpl.DPLAddLinkToEmbeddedFile(self.instanceID, Left, Top, Width, Height, EmbeddedFileID, Title, Contents, IconType, Transpareny)
    return result

  def AddLinkToFile(self, Left, Top, Width, Height, FileName, Page, Position, NewWindow, Options):
    result = self.dpl.DPLAddLinkToFile(self.instanceID, Left, Top, Width, Height, FileName, Page, Position, NewWindow, Options)
    return result

  def AddLinkToFileDest(self, Left, Top, Width, Height, FileName, NamedDest, Position, NewWindow, Options):
    result = self.dpl.DPLAddLinkToFileDest(self.instanceID, Left, Top, Width, Height, FileName, NamedDest, Position, NewWindow, Options)
    return result

  def AddLinkToFileEx(self, Left, Top, Width, Height, FileName, DestPage, NewWindow, Options, Zoom, DestType, DestLeft, DestTop, DestRight, DestBottom):
    result = self.dpl.DPLAddLinkToFileEx(self.instanceID, Left, Top, Width, Height, FileName, DestPage, NewWindow, Options, Zoom, DestType, DestLeft, DestTop, DestRight, DestBottom)
    return result

  def AddLinkToJavaScript(self, Left, Top, Width, Height, JavaScript, Options):
    result = self.dpl.DPLAddLinkToJavaScript(self.instanceID, Left, Top, Width, Height, JavaScript, Options)
    return result

  def AddLinkToLocalFile(self, Left, Top, Width, Height, FileName, Options):
    result = self.dpl.DPLAddLinkToLocalFile(self.instanceID, Left, Top, Width, Height, FileName, Options)
    return result

  def AddLinkToPage(self, Left, Top, Width, Height, Page, Position, Options):
    result = self.dpl.DPLAddLinkToPage(self.instanceID, Left, Top, Width, Height, Page, Position, Options)
    return result

  def AddLinkToWeb(self, Left, Top, Width, Height, Link, Options):
    result = self.dpl.DPLAddLinkToWeb(self.instanceID, Left, Top, Width, Height, Link, Options)
    return result

  def AddNoteAnnotation(self, Left, Top, AnnotType, PopupLeft, PopupTop, PopupWidth, PopupHeight, Title, Contents, Red, Green, Blue, Open):
    result = self.dpl.DPLAddNoteAnnotation(self.instanceID, Left, Top, AnnotType, PopupLeft, PopupTop, PopupWidth, PopupHeight, Title, Contents, Red, Green, Blue, Open)
    return result

  def AddOpenTypeFontFromFile(self, FileName, Options):
    result = self.dpl.DPLAddOpenTypeFontFromFile(self.instanceID, FileName, Options)
    return result

  def AddOpenTypeFontFromString(self, Source, Options):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLAddOpenTypeFontFromString(self.instanceID, SourceBuffer, Options)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def AddPageLabels(self, Start, Style, Offset, Prefix):
    result = self.dpl.DPLAddPageLabels(self.instanceID, Start, Style, Offset, Prefix)
    return result

  def AddPageMatrix(self, xscale, yscale, xoffset, yoffset):
    result = self.dpl.DPLAddPageMatrix(self.instanceID, xscale, yscale, xoffset, yoffset)
    return result

  def AddRGBSeparationColor(self, ColorName, Red, Green, Blue, Options):
    result = self.dpl.DPLAddRGBSeparationColor(self.instanceID, ColorName, Red, Green, Blue, Options)
    return result

  def AddRelativeLinkToFile(self, Left, Top, Width, Height, FileName, Page, Position, NewWindow, Options):
    result = self.dpl.DPLAddRelativeLinkToFile(self.instanceID, Left, Top, Width, Height, FileName, Page, Position, NewWindow, Options)
    return result

  def AddRelativeLinkToFileDest(self, Left, Top, Width, Height, FileName, NamedDest, Position, NewWindow, Options):
    result = self.dpl.DPLAddRelativeLinkToFileDest(self.instanceID, Left, Top, Width, Height, FileName, NamedDest, Position, NewWindow, Options)
    return result

  def AddRelativeLinkToFileEx(self, Left, Top, Width, Height, FileName, DestPage, NewWindow, Options, Zoom, DestType, DestLeft, DestTop, DestRight, DestBottom):
    result = self.dpl.DPLAddRelativeLinkToFileEx(self.instanceID, Left, Top, Width, Height, FileName, DestPage, NewWindow, Options, Zoom, DestType, DestLeft, DestTop, DestRight, DestBottom)
    return result

  def AddRelativeLinkToLocalFile(self, Left, Top, Width, Height, FileName, Options):
    result = self.dpl.DPLAddRelativeLinkToLocalFile(self.instanceID, Left, Top, Width, Height, FileName, Options)
    return result

  def AddSVGAnnotationFromFile(self, Left, Top, Width, Height, FileName, Options):
    result = self.dpl.DPLAddSVGAnnotationFromFile(self.instanceID, Left, Top, Width, Height, FileName, Options)
    return result

  def AddSWFAnnotationFromFile(self, Left, Top, Width, Height, FileName, Title, Options):
    result = self.dpl.DPLAddSWFAnnotationFromFile(self.instanceID, Left, Top, Width, Height, FileName, Title, Options)
    return result

  def AddSeparationColor(self, ColorName, C, M, Y, K, Options):
    result = self.dpl.DPLAddSeparationColor(self.instanceID, ColorName, C, M, Y, K, Options)
    return result

  def AddSignProcessOverlayText(self, SignProcessID, XPos, YPos, TextSize, LayerName, OverlayText):
    result = self.dpl.DPLAddSignProcessOverlayText(self.instanceID, SignProcessID, XPos, YPos, TextSize, LayerName, OverlayText)
    return result

  def AddStampAnnotation(self, Left, Top, Width, Height, StampType, Title, Contents, Red, Green, Blue, Options):
    result = self.dpl.DPLAddStampAnnotation(self.instanceID, Left, Top, Width, Height, StampType, Title, Contents, Red, Green, Blue, Options)
    return result

  def AddStampAnnotationFromImage(self, Left, Top, Width, Height, FileName, Title, Contents, Red, Green, Blue, Options):
    result = self.dpl.DPLAddStampAnnotationFromImage(self.instanceID, Left, Top, Width, Height, FileName, Title, Contents, Red, Green, Blue, Options)
    return result

  def AddStampAnnotationFromImageID(self, Left, Top, Width, Height, ImageID, Title, Contents, Red, Green, Blue, Options):
    result = self.dpl.DPLAddStampAnnotationFromImageID(self.instanceID, Left, Top, Width, Height, ImageID, Title, Contents, Red, Green, Blue, Options)
    return result

  def AddStandardFont(self, StandardFontID):
    result = self.dpl.DPLAddStandardFont(self.instanceID, StandardFontID)
    return result

  def AddSubsettedFont(self, FontName, CharsetIndex, SubsetChars):
    result = self.dpl.DPLAddSubsettedFont(self.instanceID, FontName, CharsetIndex, SubsetChars)
    return result

  def AddTextMarkupAnnotation(self, MarkupType, Left, Top, Width, Height):
    result = self.dpl.DPLAddTextMarkupAnnotation(self.instanceID, MarkupType, Left, Top, Width, Height)
    return result

  def AddToBuffer(self, Buffer, Source, SourceLength):
    BufferBuffer, BufferUsed = self.StringParm(Buffer)
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLAddToBuffer(self.instanceID, BufferBuffer, SourceBuffer, SourceLength)
    if BufferUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, BufferBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def AddToFileList(self, ListName, FileName):
    result = self.dpl.DPLAddToFileList(self.instanceID, ListName, FileName)
    return result

  def AddToUnicodeFontGroup(self, FontGroupName, FontID):
    result = self.dpl.DPLAddToUnicodeFontGroup(self.instanceID, FontGroupName, FontID)
    return result

  def AddTrueTypeFont(self, FontName, Embed):
    result = self.dpl.DPLAddTrueTypeFont(self.instanceID, FontName, Embed)
    return result

  def AddTrueTypeFontFromFile(self, FileName):
    result = self.dpl.DPLAddTrueTypeFontFromFile(self.instanceID, FileName)
    return result

  def AddTrueTypeFontFromFileEx(self, FileName, Options):
    result = self.dpl.DPLAddTrueTypeFontFromFileEx(self.instanceID, FileName, Options)
    return result

  def AddTrueTypeFontFromString(self, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLAddTrueTypeFontFromString(self.instanceID, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def AddTrueTypeFontFromStringEx(self, Source, Options):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLAddTrueTypeFontFromStringEx(self.instanceID, SourceBuffer, Options)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def AddTrueTypeSubsettedFont(self, FontName, SubsetChars, Options):
    result = self.dpl.DPLAddTrueTypeSubsettedFont(self.instanceID, FontName, SubsetChars, Options)
    return result

  def AddTrueTypeSubsettedFontFromFile(self, FileName, SubsetChars, Options):
    result = self.dpl.DPLAddTrueTypeSubsettedFontFromFile(self.instanceID, FileName, SubsetChars, Options)
    return result

  def AddTrueTypeSubsettedFontFromString(self, Source, SubsetChars, Options):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLAddTrueTypeSubsettedFontFromString(self.instanceID, SourceBuffer, SubsetChars, Options)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def AddType1Font(self, FileName):
    result = self.dpl.DPLAddType1Font(self.instanceID, FileName)
    return result

  def AddU3DAnnotationFromFile(self, Left, Top, Width, Height, FileName, Options):
    result = self.dpl.DPLAddU3DAnnotationFromFile(self.instanceID, Left, Top, Width, Height, FileName, Options)
    return result

  def AddUnicodeFont(self, FontName, EncodingOptions, EmbedOptions):
    result = self.dpl.DPLAddUnicodeFont(self.instanceID, FontName, EncodingOptions, EmbedOptions)
    return result

  def AddUnicodeFontFromFile(self, FontFileName, EncodingOptions, EmbedOptions):
    result = self.dpl.DPLAddUnicodeFontFromFile(self.instanceID, FontFileName, EncodingOptions, EmbedOptions)
    return result

  def AnalyseFile(self, InputFileName, Password):
    result = self.dpl.DPLAnalyseFile(self.instanceID, InputFileName, Password)
    return result

  def AnnotationCount(self):
    result = self.dpl.DPLAnnotationCount(self.instanceID)
    return result

  def AnsiStringResultLength(self):
    result = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    return result

  def AppendSpace(self, RelativeSpace):
    result = self.dpl.DPLAppendSpace(self.instanceID, RelativeSpace)
    return result

  def AppendTableColumns(self, TableID, NewColumnCount):
    result = self.dpl.DPLAppendTableColumns(self.instanceID, TableID, NewColumnCount)
    return result

  def AppendTableRows(self, TableID, NewRowCount):
    result = self.dpl.DPLAppendTableRows(self.instanceID, TableID, NewRowCount)
    return result

  def AppendText(self, Text):
    result = self.dpl.DPLAppendText(self.instanceID, Text)
    return result

  def AppendToFile(self, FileName):
    result = self.dpl.DPLAppendToFile(self.instanceID, FileName)
    return result

  def AppendToString(self, AppendMode):
    resultPtr = self.dpl.DPLAppendToString(self.instanceID, AppendMode)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def ApplyStyle(self, StyleName):
    result = self.dpl.DPLApplyStyle(self.instanceID, StyleName)
    return result

  def AttachAnnotToForm(self, Index):
    result = self.dpl.DPLAttachAnnotToForm(self.instanceID, Index)
    return result

  def BalanceContentStream(self):
    result = self.dpl.DPLBalanceContentStream(self.instanceID)
    return result

  def BalancePageTree(self, Options):
    result = self.dpl.DPLBalancePageTree(self.instanceID, Options)
    return result

  def BeginPageUpdate(self):
    result = self.dpl.DPLBeginPageUpdate(self.instanceID)
    return result

  def CapturePage(self, Page):
    result = self.dpl.DPLCapturePage(self.instanceID, Page)
    return result

  def CapturePageEx(self, Page, Options):
    result = self.dpl.DPLCapturePageEx(self.instanceID, Page, Options)
    return result

  def CharWidth(self, CharCode):
    result = self.dpl.DPLCharWidth(self.instanceID, CharCode)
    return result

  def CheckFileCompliance(self, InputFileName, Password, ComplianceTest, Options):
    result = self.dpl.DPLCheckFileCompliance(self.instanceID, InputFileName, Password, ComplianceTest, Options)
    return result

  def CheckObjects(self):
    result = self.dpl.DPLCheckObjects(self.instanceID)
    return result

  def CheckPageAnnots(self):
    result = self.dpl.DPLCheckPageAnnots(self.instanceID)
    return result

  def CheckPassword(self, Password):
    result = self.dpl.DPLCheckPassword(self.instanceID, Password)
    return result

  def ClearFileList(self, ListName):
    result = self.dpl.DPLClearFileList(self.instanceID, ListName)
    return result

  def ClearImage(self, ImageID):
    result = self.dpl.DPLClearImage(self.instanceID, ImageID)
    return result

  def ClearPageLabels(self):
    result = self.dpl.DPLClearPageLabels(self.instanceID)
    return result

  def ClearTextFormatting(self):
    result = self.dpl.DPLClearTextFormatting(self.instanceID)
    return result

  def CloneOutlineAction(self, OutlineID):
    result = self.dpl.DPLCloneOutlineAction(self.instanceID, OutlineID)
    return result

  def ClonePages(self, StartPage, EndPage, RepeatCount):
    result = self.dpl.DPLClonePages(self.instanceID, StartPage, EndPage, RepeatCount)
    return result

  def CloseOutline(self, OutlineID):
    result = self.dpl.DPLCloseOutline(self.instanceID, OutlineID)
    return result

  def ClosePath(self):
    result = self.dpl.DPLClosePath(self.instanceID)
    return result

  def CombineContentStreams(self):
    result = self.dpl.DPLCombineContentStreams(self.instanceID)
    return result

  def CompareOutlines(self, FirstOutlineID, SecondOutlineID):
    result = self.dpl.DPLCompareOutlines(self.instanceID, FirstOutlineID, SecondOutlineID)
    return result

  def CompressContent(self):
    result = self.dpl.DPLCompressContent(self.instanceID)
    return result

  def CompressFonts(self, Compress):
    result = self.dpl.DPLCompressFonts(self.instanceID, Compress)
    return result

  def CompressImages(self, Compress):
    result = self.dpl.DPLCompressImages(self.instanceID, Compress)
    return result

  def CompressPage(self):
    result = self.dpl.DPLCompressPage(self.instanceID)
    return result

  def ContentStreamCount(self):
    result = self.dpl.DPLContentStreamCount(self.instanceID)
    return result

  def ContentStreamSafe(self):
    result = self.dpl.DPLContentStreamSafe(self.instanceID)
    return result

  def CopyPageRanges(self, DocumentID, RangeList):
    result = self.dpl.DPLCopyPageRanges(self.instanceID, DocumentID, RangeList)
    return result

  def CopyPageRangesEx(self, DocumentID, RangeList, Options):
    result = self.dpl.DPLCopyPageRangesEx(self.instanceID, DocumentID, RangeList, Options)
    return result

  def CreateBuffer(self, BufferLength):
    resultPtr = self.dpl.DPLCreateBuffer(self.instanceID, BufferLength)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def CreateNewObject(self):
    result = self.dpl.DPLCreateNewObject(self.instanceID)
    return result

  def CreateRenderer(self):
    result = self.dpl.DPLCreateRenderer(self.instanceID)
    return result

  def CreateTable(self, RowCount, ColumnCount):
    result = self.dpl.DPLCreateTable(self.instanceID, RowCount, ColumnCount)
    return result

  def DAAppendFile(self, FileHandle):
    result = self.dpl.DPLDAAppendFile(self.instanceID, FileHandle)
    return result

  def DACapturePage(self, FileHandle, PageRef):
    result = self.dpl.DPLDACapturePage(self.instanceID, FileHandle, PageRef)
    return result

  def DACapturePageEx(self, FileHandle, PageRef, Options):
    result = self.dpl.DPLDACapturePageEx(self.instanceID, FileHandle, PageRef, Options)
    return result

  def DACloseFile(self, FileHandle):
    result = self.dpl.DPLDACloseFile(self.instanceID, FileHandle)
    return result

  def DADrawCapturedPage(self, FileHandle, DACaptureID, DestPageRef, PntLeft, PntBottom, PntWidth, PntHeight):
    result = self.dpl.DPLDADrawCapturedPage(self.instanceID, FileHandle, DACaptureID, DestPageRef, PntLeft, PntBottom, PntWidth, PntHeight)
    return result

  def DADrawRotatedCapturedPage(self, FileHandle, DACaptureID, DestPageRef, PntLeft, PntBottom, PntWidth, PntHeight, Angle):
    result = self.dpl.DPLDADrawRotatedCapturedPage(self.instanceID, FileHandle, DACaptureID, DestPageRef, PntLeft, PntBottom, PntWidth, PntHeight, Angle)
    return result

  def DAEmbedFileStreams(self, FileHandle, RootPath):
    result = self.dpl.DPLDAEmbedFileStreams(self.instanceID, FileHandle, RootPath)
    return result

  def DAExtractPageText(self, FileHandle, PageRef, Options):
    result = self.dpl.DPLDAExtractPageText(self.instanceID, FileHandle, PageRef, Options)
    return result

  def DAExtractPageTextBlocks(self, FileHandle, PageRef, ExtractOptions):
    result = self.dpl.DPLDAExtractPageTextBlocks(self.instanceID, FileHandle, PageRef, ExtractOptions)
    return result

  def DAFindPage(self, FileHandle, Page):
    result = self.dpl.DPLDAFindPage(self.instanceID, FileHandle, Page)
    return result

  def DAGetAnnotationCount(self, FileHandle, PageRef):
    result = self.dpl.DPLDAGetAnnotationCount(self.instanceID, FileHandle, PageRef)
    return result

  def DAGetFormFieldCount(self, FileHandle):
    result = self.dpl.DPLDAGetFormFieldCount(self.instanceID, FileHandle)
    return result

  def DAGetFormFieldTitle(self, FileHandle, FieldIndex):
    result = self.dpl.DPLDAGetFormFieldTitle(self.instanceID, FileHandle, FieldIndex)
    return result

  def DAGetFormFieldValue(self, FileHandle, FieldIndex):
    result = self.dpl.DPLDAGetFormFieldValue(self.instanceID, FileHandle, FieldIndex)
    return result

  def DAGetImageDataToString(self, FileHandle, ImageListID, ImageIndex):
    resultPtr = self.dpl.DPLDAGetImageDataToString(self.instanceID, FileHandle, ImageListID, ImageIndex)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def DAGetImageDblProperty(self, FileHandle, ImageListID, ImageIndex, PropertyID):
    result = self.dpl.DPLDAGetImageDblProperty(self.instanceID, FileHandle, ImageListID, ImageIndex, PropertyID)
    return result

  def DAGetImageIntProperty(self, FileHandle, ImageListID, ImageIndex, PropertyID):
    result = self.dpl.DPLDAGetImageIntProperty(self.instanceID, FileHandle, ImageListID, ImageIndex, PropertyID)
    return result

  def DAGetImageListCount(self, FileHandle, ImageListID):
    result = self.dpl.DPLDAGetImageListCount(self.instanceID, FileHandle, ImageListID)
    return result

  def DAGetInformation(self, FileHandle, Key):
    result = self.dpl.DPLDAGetInformation(self.instanceID, FileHandle, Key)
    return result

  def DAGetObjectCount(self, FileHandle):
    result = self.dpl.DPLDAGetObjectCount(self.instanceID, FileHandle)
    return result

  def DAGetObjectToString(self, FileHandle, ObjectNumber):
    resultPtr = self.dpl.DPLDAGetObjectToString(self.instanceID, FileHandle, ObjectNumber)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def DAGetPageBox(self, FileHandle, PageRef, BoxIndex, Dimension):
    result = self.dpl.DPLDAGetPageBox(self.instanceID, FileHandle, PageRef, BoxIndex, Dimension)
    return result

  def DAGetPageContentToString(self, FileHandle, PageRef):
    resultPtr = self.dpl.DPLDAGetPageContentToString(self.instanceID, FileHandle, PageRef)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def DAGetPageCount(self, FileHandle):
    result = self.dpl.DPLDAGetPageCount(self.instanceID, FileHandle)
    return result

  def DAGetPageHeight(self, FileHandle, PageRef):
    result = self.dpl.DPLDAGetPageHeight(self.instanceID, FileHandle, PageRef)
    return result

  def DAGetPageImageList(self, FileHandle, PageRef):
    result = self.dpl.DPLDAGetPageImageList(self.instanceID, FileHandle, PageRef)
    return result

  def DAGetPageLayout(self, FileHandle):
    result = self.dpl.DPLDAGetPageLayout(self.instanceID, FileHandle)
    return result

  def DAGetPageMode(self, FileHandle):
    result = self.dpl.DPLDAGetPageMode(self.instanceID, FileHandle)
    return result

  def DAGetPageWidth(self, FileHandle, PageRef):
    result = self.dpl.DPLDAGetPageWidth(self.instanceID, FileHandle, PageRef)
    return result

  def DAGetTextBlockAsString(self, TextBlockListID, Index):
    result = self.dpl.DPLDAGetTextBlockAsString(self.instanceID, TextBlockListID, Index)
    return result

  def DAGetTextBlockBound(self, TextBlockListID, Index, BoundIndex):
    result = self.dpl.DPLDAGetTextBlockBound(self.instanceID, TextBlockListID, Index, BoundIndex)
    return result

  def DAGetTextBlockCharWidth(self, TextBlockListID, Index, CharIndex):
    result = self.dpl.DPLDAGetTextBlockCharWidth(self.instanceID, TextBlockListID, Index, CharIndex)
    return result

  def DAGetTextBlockColor(self, TextBlockListID, Index, ColorComponent):
    result = self.dpl.DPLDAGetTextBlockColor(self.instanceID, TextBlockListID, Index, ColorComponent)
    return result

  def DAGetTextBlockColorType(self, TextBlockListID, Index):
    result = self.dpl.DPLDAGetTextBlockColorType(self.instanceID, TextBlockListID, Index)
    return result

  def DAGetTextBlockCount(self, TextBlockListID):
    result = self.dpl.DPLDAGetTextBlockCount(self.instanceID, TextBlockListID)
    return result

  def DAGetTextBlockFontName(self, TextBlockListID, Index):
    result = self.dpl.DPLDAGetTextBlockFontName(self.instanceID, TextBlockListID, Index)
    return result

  def DAGetTextBlockFontSize(self, TextBlockListID, Index):
    result = self.dpl.DPLDAGetTextBlockFontSize(self.instanceID, TextBlockListID, Index)
    return result

  def DAGetTextBlockText(self, TextBlockListID, Index):
    result = self.dpl.DPLDAGetTextBlockText(self.instanceID, TextBlockListID, Index)
    return result

  def DAHasPageBox(self, FileHandle, PageRef, BoxIndex):
    result = self.dpl.DPLDAHasPageBox(self.instanceID, FileHandle, PageRef, BoxIndex)
    return result

  def DAHidePage(self, FileHandle, PageRef):
    result = self.dpl.DPLDAHidePage(self.instanceID, FileHandle, PageRef)
    return result

  def DAMovePage(self, FileHandle, PageRef, TargetPageRef, Options):
    result = self.dpl.DPLDAMovePage(self.instanceID, FileHandle, PageRef, TargetPageRef, Options)
    return result

  def DANewPage(self, FileHandle):
    result = self.dpl.DPLDANewPage(self.instanceID, FileHandle)
    return result

  def DANewPages(self, FileHandle, PageCount):
    result = self.dpl.DPLDANewPages(self.instanceID, FileHandle, PageCount)
    return result

  def DANormalizePage(self, FileHandle, PageRef, NormalizeOptions):
    result = self.dpl.DPLDANormalizePage(self.instanceID, FileHandle, PageRef, NormalizeOptions)
    return result

  def DAOpenFile(self, InputFileName, Password):
    result = self.dpl.DPLDAOpenFile(self.instanceID, InputFileName, Password)
    return result

  def DAOpenFileReadOnly(self, InputFileName, Password):
    result = self.dpl.DPLDAOpenFileReadOnly(self.instanceID, InputFileName, Password)
    return result

  def DAPageRotation(self, FileHandle, PageRef):
    result = self.dpl.DPLDAPageRotation(self.instanceID, FileHandle, PageRef)
    return result

  def DAReleaseImageList(self, FileHandle, ImageListID):
    result = self.dpl.DPLDAReleaseImageList(self.instanceID, FileHandle, ImageListID)
    return result

  def DAReleaseTextBlocks(self, TextBlockListID):
    result = self.dpl.DPLDAReleaseTextBlocks(self.instanceID, TextBlockListID)
    return result

  def DARemoveUsageRights(self, FileHandle):
    result = self.dpl.DPLDARemoveUsageRights(self.instanceID, FileHandle)
    return result

  def DARenderPageToDC(self, FileHandle, PageRef, DPI, DC):
    result = self.dpl.DPLDARenderPageToDC(self.instanceID, FileHandle, PageRef, DPI, DC)
    return result

  def DARenderPageToFile(self, FileHandle, PageRef, Options, DPI, FileName):
    result = self.dpl.DPLDARenderPageToFile(self.instanceID, FileHandle, PageRef, Options, DPI, FileName)
    return result

  def DARenderPageToString(self, FileHandle, PageRef, Options, DPI):
    resultPtr = self.dpl.DPLDARenderPageToString(self.instanceID, FileHandle, PageRef, Options, DPI)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def DARotatePage(self, FileHandle, PageRef, Angle, Options):
    result = self.dpl.DPLDARotatePage(self.instanceID, FileHandle, PageRef, Angle, Options)
    return result

  def DASaveAsFile(self, FileHandle, OutputFileName):
    result = self.dpl.DPLDASaveAsFile(self.instanceID, FileHandle, OutputFileName)
    return result

  def DASaveImageDataToFile(self, FileHandle, ImageListID, ImageIndex, ImageFileName):
    result = self.dpl.DPLDASaveImageDataToFile(self.instanceID, FileHandle, ImageListID, ImageIndex, ImageFileName)
    return result

  def DASetInformation(self, FileHandle, Key, NewValue):
    result = self.dpl.DPLDASetInformation(self.instanceID, FileHandle, Key, NewValue)
    return result

  def DASetPageBox(self, FileHandle, PageRef, BoxIndex, X1, Y1, X2, Y2):
    result = self.dpl.DPLDASetPageBox(self.instanceID, FileHandle, PageRef, BoxIndex, X1, Y1, X2, Y2)
    return result

  def DASetPageLayout(self, FileHandle, NewPageLayout):
    result = self.dpl.DPLDASetPageLayout(self.instanceID, FileHandle, NewPageLayout)
    return result

  def DASetPageMode(self, FileHandle, NewPageMode):
    result = self.dpl.DPLDASetPageMode(self.instanceID, FileHandle, NewPageMode)
    return result

  def DASetPageSize(self, FileHandle, PageRef, PntWidth, PntHeight):
    result = self.dpl.DPLDASetPageSize(self.instanceID, FileHandle, PageRef, PntWidth, PntHeight)
    return result

  def DASetRenderArea(self, Left, Top, Width, Height):
    result = self.dpl.DPLDASetRenderArea(self.instanceID, Left, Top, Width, Height)
    return result

  def DASetTextExtractionArea(self, Left, Top, Width, Height):
    result = self.dpl.DPLDASetTextExtractionArea(self.instanceID, Left, Top, Width, Height)
    return result

  def DASetTextExtractionOptions(self, OptionID, NewValue):
    result = self.dpl.DPLDASetTextExtractionOptions(self.instanceID, OptionID, NewValue)
    return result

  def DASetTextExtractionScaling(self, Options, Horizontal, Vertical):
    result = self.dpl.DPLDASetTextExtractionScaling(self.instanceID, Options, Horizontal, Vertical)
    return result

  def DASetTextExtractionWordGap(self, NewWordGap):
    result = self.dpl.DPLDASetTextExtractionWordGap(self.instanceID, NewWordGap)
    return result

  def DAShiftedHeader(self, FileHandle):
    result = self.dpl.DPLDAShiftedHeader(self.instanceID, FileHandle)
    return result

  def Decrypt(self):
    result = self.dpl.DPLDecrypt(self.instanceID)
    return result

  def DecryptFile(self, InputFileName, OutputFileName, Password):
    result = self.dpl.DPLDecryptFile(self.instanceID, InputFileName, OutputFileName, Password)
    return result

  def DeleteAnalysis(self, AnalysisID):
    result = self.dpl.DPLDeleteAnalysis(self.instanceID, AnalysisID)
    return result

  def DeleteAnnotation(self, Index):
    result = self.dpl.DPLDeleteAnnotation(self.instanceID, Index)
    return result

  def DeleteContentStream(self):
    result = self.dpl.DPLDeleteContentStream(self.instanceID)
    return result

  def DeleteFormField(self, Index):
    result = self.dpl.DPLDeleteFormField(self.instanceID, Index)
    return result

  def DeleteOptionalContentGroup(self, OptionalContentGroupID):
    result = self.dpl.DPLDeleteOptionalContentGroup(self.instanceID, OptionalContentGroupID)
    return result

  def DeletePageLGIDict(self, DictIndex):
    result = self.dpl.DPLDeletePageLGIDict(self.instanceID, DictIndex)
    return result

  def DeletePages(self, StartPage, PageCount):
    result = self.dpl.DPLDeletePages(self.instanceID, StartPage, PageCount)
    return result

  def DestroyRenderer(self):
    result = self.dpl.DPLDestroyRenderer(self.instanceID)
    return result

  def DocJavaScriptAction(self, ActionType, JavaScript):
    result = self.dpl.DPLDocJavaScriptAction(self.instanceID, ActionType, JavaScript)
    return result

  def DocumentCount(self):
    result = self.dpl.DPLDocumentCount(self.instanceID)
    return result

  def DrawArc(self, XPos, YPos, Radius, StartAngle, EndAngle, Pie, DrawOptions):
    result = self.dpl.DPLDrawArc(self.instanceID, XPos, YPos, Radius, StartAngle, EndAngle, Pie, DrawOptions)
    return result

  def DrawBarcode(self, Left, Top, Width, Height, Text, Barcode, Options):
    result = self.dpl.DPLDrawBarcode(self.instanceID, Left, Top, Width, Height, Text, Barcode, Options)
    return result

  def DrawBox(self, Left, Top, Width, Height, DrawOptions):
    result = self.dpl.DPLDrawBox(self.instanceID, Left, Top, Width, Height, DrawOptions)
    return result

  def DrawCapturedPage(self, CaptureID, Left, Top, Width, Height):
    result = self.dpl.DPLDrawCapturedPage(self.instanceID, CaptureID, Left, Top, Width, Height)
    return result

  def DrawCapturedPageMatrix(self, CaptureID, M11, M12, M21, M22, MDX, MDY):
    result = self.dpl.DPLDrawCapturedPageMatrix(self.instanceID, CaptureID, M11, M12, M21, M22, MDX, MDY)
    return result

  def DrawCircle(self, XPos, YPos, Radius, DrawOptions):
    result = self.dpl.DPLDrawCircle(self.instanceID, XPos, YPos, Radius, DrawOptions)
    return result

  def DrawDataMatrixSymbol(self, Left, Top, ModuleSize, Text, Encoding, SymbolSize, Options):
    result = self.dpl.DPLDrawDataMatrixSymbol(self.instanceID, Left, Top, ModuleSize, Text, Encoding, SymbolSize, Options)
    return result

  def DrawEllipse(self, XPos, YPos, Width, Height, DrawOptions):
    result = self.dpl.DPLDrawEllipse(self.instanceID, XPos, YPos, Width, Height, DrawOptions)
    return result

  def DrawEllipticArc(self, XPos, YPos, Width, Height, StartAngle, EndAngle, Pie, DrawOptions):
    result = self.dpl.DPLDrawEllipticArc(self.instanceID, XPos, YPos, Width, Height, StartAngle, EndAngle, Pie, DrawOptions)
    return result

  def DrawFontGroupText(self, FontGroupName, XPos, YPos, Text):
    result = self.dpl.DPLDrawFontGroupText(self.instanceID, FontGroupName, XPos, YPos, Text)
    return result

  def DrawHTMLText(self, Left, Top, Width, HTMLText):
    result = self.dpl.DPLDrawHTMLText(self.instanceID, Left, Top, Width, HTMLText)
    return result

  def DrawHTMLTextBox(self, Left, Top, Width, Height, HTMLText):
    result = self.dpl.DPLDrawHTMLTextBox(self.instanceID, Left, Top, Width, Height, HTMLText)
    return result

  def DrawHTMLTextBoxMatrix(self, Width, Height, HTMLText, M11, M12, M21, M22, MDX, MDY):
    result = self.dpl.DPLDrawHTMLTextBoxMatrix(self.instanceID, Width, Height, HTMLText, M11, M12, M21, M22, MDX, MDY)
    return result

  def DrawHTMLTextMatrix(self, Width, HTMLText, M11, M12, M21, M22, MDX, MDY):
    result = self.dpl.DPLDrawHTMLTextMatrix(self.instanceID, Width, HTMLText, M11, M12, M21, M22, MDX, MDY)
    return result

  def DrawImage(self, Left, Top, Width, Height):
    result = self.dpl.DPLDrawImage(self.instanceID, Left, Top, Width, Height)
    return result

  def DrawImageMatrix(self, M11, M12, M21, M22, MDX, MDY):
    result = self.dpl.DPLDrawImageMatrix(self.instanceID, M11, M12, M21, M22, MDX, MDY)
    return result

  def DrawIntelligentMailBarcode(self, Left, Top, BarWidth, FullBarHeight, TrackerHeight, SpaceWidth, BarcodeData, Options):
    result = self.dpl.DPLDrawIntelligentMailBarcode(self.instanceID, Left, Top, BarWidth, FullBarHeight, TrackerHeight, SpaceWidth, BarcodeData, Options)
    return result

  def DrawLine(self, StartX, StartY, EndX, EndY):
    result = self.dpl.DPLDrawLine(self.instanceID, StartX, StartY, EndX, EndY)
    return result

  def DrawMultiLineText(self, XPos, YPos, Delimiter, Text):
    result = self.dpl.DPLDrawMultiLineText(self.instanceID, XPos, YPos, Delimiter, Text)
    return result

  def DrawPDF417Symbol(self, Left, Top, Text, Options):
    result = self.dpl.DPLDrawPDF417Symbol(self.instanceID, Left, Top, Text, Options)
    return result

  def DrawPDF417SymbolEx(self, Left, Top, Text, Options, FixedColumns, FixedRows, ErrorLevel, ModuleSize, HeightWidthRatio):
    result = self.dpl.DPLDrawPDF417SymbolEx(self.instanceID, Left, Top, Text, Options, FixedColumns, FixedRows, ErrorLevel, ModuleSize, HeightWidthRatio)
    return result

  def DrawPath(self, PathOptions):
    result = self.dpl.DPLDrawPath(self.instanceID, PathOptions)
    return result

  def DrawPathEvenOdd(self, PathOptions):
    result = self.dpl.DPLDrawPathEvenOdd(self.instanceID, PathOptions)
    return result

  def DrawPostScriptXObject(self, PSRef):
    result = self.dpl.DPLDrawPostScriptXObject(self.instanceID, PSRef)
    return result

  def DrawQRCode(self, Left, Top, SymbolSize, Text, EncodeOptions, DrawOptions):
    result = self.dpl.DPLDrawQRCode(self.instanceID, Left, Top, SymbolSize, Text, EncodeOptions, DrawOptions)
    return result

  def DrawRotatedBox(self, Left, Bottom, Width, Height, Angle, DrawOptions):
    result = self.dpl.DPLDrawRotatedBox(self.instanceID, Left, Bottom, Width, Height, Angle, DrawOptions)
    return result

  def DrawRotatedCapturedPage(self, CaptureID, Left, Bottom, Width, Height, Angle):
    result = self.dpl.DPLDrawRotatedCapturedPage(self.instanceID, CaptureID, Left, Bottom, Width, Height, Angle)
    return result

  def DrawRotatedImage(self, Left, Bottom, Width, Height, Angle):
    result = self.dpl.DPLDrawRotatedImage(self.instanceID, Left, Bottom, Width, Height, Angle)
    return result

  def DrawRotatedMultiLineText(self, XPos, YPos, Angle, Delimiter, Text):
    result = self.dpl.DPLDrawRotatedMultiLineText(self.instanceID, XPos, YPos, Angle, Delimiter, Text)
    return result

  def DrawRotatedText(self, XPos, YPos, Angle, Text):
    result = self.dpl.DPLDrawRotatedText(self.instanceID, XPos, YPos, Angle, Text)
    return result

  def DrawRotatedTextBox(self, Left, Top, Width, Height, Angle, Text, Options):
    result = self.dpl.DPLDrawRotatedTextBox(self.instanceID, Left, Top, Width, Height, Angle, Text, Options)
    return result

  def DrawRotatedTextBoxEx(self, Left, Top, Width, Height, Angle, Text, Options, Border, Radius, DrawOptions):
    result = self.dpl.DPLDrawRotatedTextBoxEx(self.instanceID, Left, Top, Width, Height, Angle, Text, Options, Border, Radius, DrawOptions)
    return result

  def DrawRoundedBox(self, Left, Top, Width, Height, Radius, DrawOptions):
    result = self.dpl.DPLDrawRoundedBox(self.instanceID, Left, Top, Width, Height, Radius, DrawOptions)
    return result

  def DrawRoundedRotatedBox(self, Left, Bottom, Width, Height, Radius, Angle, DrawOptions):
    result = self.dpl.DPLDrawRoundedRotatedBox(self.instanceID, Left, Bottom, Width, Height, Radius, Angle, DrawOptions)
    return result

  def DrawScaledImage(self, Left, Top, Scale):
    result = self.dpl.DPLDrawScaledImage(self.instanceID, Left, Top, Scale)
    return result

  def DrawSpacedText(self, XPos, YPos, Spacing, Text):
    result = self.dpl.DPLDrawSpacedText(self.instanceID, XPos, YPos, Spacing, Text)
    return result

  def DrawTableRows(self, TableID, Left, Top, Height, FirstRow, LastRow):
    result = self.dpl.DPLDrawTableRows(self.instanceID, TableID, Left, Top, Height, FirstRow, LastRow)
    return result

  def DrawText(self, XPos, YPos, Text):
    result = self.dpl.DPLDrawText(self.instanceID, XPos, YPos, Text)
    return result

  def DrawTextArc(self, XPos, YPos, Radius, Angle, Text, DrawOptions):
    result = self.dpl.DPLDrawTextArc(self.instanceID, XPos, YPos, Radius, Angle, Text, DrawOptions)
    return result

  def DrawTextBox(self, Left, Top, Width, Height, Text, Options):
    result = self.dpl.DPLDrawTextBox(self.instanceID, Left, Top, Width, Height, Text, Options)
    return result

  def DrawTextBoxMatrix(self, Width, Height, Text, Options, M11, M12, M21, M22, MDX, MDY):
    result = self.dpl.DPLDrawTextBoxMatrix(self.instanceID, Width, Height, Text, Options, M11, M12, M21, M22, MDX, MDY)
    return result

  def DrawUniscribeText(self, XPos, YPos, Text, Options):
    result = self.dpl.DPLDrawUniscribeText(self.instanceID, XPos, YPos, Text, Options)
    return result

  def DrawWrappedText(self, XPos, YPos, Width, Text):
    result = self.dpl.DPLDrawWrappedText(self.instanceID, XPos, YPos, Width, Text)
    return result

  def EditableContentStream(self):
    result = self.dpl.DPLEditableContentStream(self.instanceID)
    return result

  def EmbedFile(self, Title, FileName, MIMEType):
    result = self.dpl.DPLEmbedFile(self.instanceID, Title, FileName, MIMEType)
    return result

  def EmbedRelatedFile(self, Title, FileName, MIMEType, AFRelationship, Options):
    result = self.dpl.DPLEmbedRelatedFile(self.instanceID, Title, FileName, MIMEType, AFRelationship, Options)
    return result

  def EmbeddedFileCount(self):
    result = self.dpl.DPLEmbeddedFileCount(self.instanceID)
    return result

  def EncapsulateContentStream(self):
    result = self.dpl.DPLEncapsulateContentStream(self.instanceID)
    return result

  def EncodePermissions(self, CanPrint, CanCopy, CanChange, CanAddNotes, CanFillFields, CanCopyAccess, CanAssemble, CanPrintFull):
    result = self.dpl.DPLEncodePermissions(self.instanceID, CanPrint, CanCopy, CanChange, CanAddNotes, CanFillFields, CanCopyAccess, CanAssemble, CanPrintFull)
    return result

  def Encrypt(self, Owner, User, Strength, Permissions):
    result = self.dpl.DPLEncrypt(self.instanceID, Owner, User, Strength, Permissions)
    return result

  def EncryptFile(self, InputFileName, OutputFileName, Owner, User, Strength, Permissions):
    result = self.dpl.DPLEncryptFile(self.instanceID, InputFileName, OutputFileName, Owner, User, Strength, Permissions)
    return result

  def EncryptWithFingerprint(self, Fingerprint):
    result = self.dpl.DPLEncryptWithFingerprint(self.instanceID, Fingerprint)
    return result

  def EncryptionAlgorithm(self):
    result = self.dpl.DPLEncryptionAlgorithm(self.instanceID)
    return result

  def EncryptionStatus(self):
    result = self.dpl.DPLEncryptionStatus(self.instanceID)
    return result

  def EncryptionStrength(self):
    result = self.dpl.DPLEncryptionStrength(self.instanceID)
    return result

  def EndPageUpdate(self):
    result = self.dpl.DPLEndPageUpdate(self.instanceID)
    return result

  def EndSignProcessToFile(self, SignProcessID, OutputFile):
    result = self.dpl.DPLEndSignProcessToFile(self.instanceID, SignProcessID, OutputFile)
    return result

  def EndSignProcessToString(self, SignProcessID):
    resultPtr = self.dpl.DPLEndSignProcessToString(self.instanceID, SignProcessID)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def ExtractFilePageContentToString(self, InputFileName, Password, Page):
    resultPtr = self.dpl.DPLExtractFilePageContentToString(self.instanceID, InputFileName, Password, Page)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def ExtractFilePageText(self, InputFileName, Password, Page, Options):
    result = self.dpl.DPLExtractFilePageText(self.instanceID, InputFileName, Password, Page, Options)
    return result

  def ExtractFilePageTextBlocks(self, InputFileName, Password, Page, Options):
    result = self.dpl.DPLExtractFilePageTextBlocks(self.instanceID, InputFileName, Password, Page, Options)
    return result

  def ExtractFilePages(self, InputFileName, Password, OutputFileName, RangeList):
    result = self.dpl.DPLExtractFilePages(self.instanceID, InputFileName, Password, OutputFileName, RangeList)
    return result

  def ExtractFilePagesEx(self, InputFileName, Password, OutputFileName, RangeList, Options):
    result = self.dpl.DPLExtractFilePagesEx(self.instanceID, InputFileName, Password, OutputFileName, RangeList, Options)
    return result

  def ExtractPageRanges(self, RangeList):
    result = self.dpl.DPLExtractPageRanges(self.instanceID, RangeList)
    return result

  def ExtractPageTextBlocks(self, ExtractOptions):
    result = self.dpl.DPLExtractPageTextBlocks(self.instanceID, ExtractOptions)
    return result

  def ExtractPages(self, StartPage, PageCount):
    result = self.dpl.DPLExtractPages(self.instanceID, StartPage, PageCount)
    return result

  def FileListCount(self, ListName):
    result = self.dpl.DPLFileListCount(self.instanceID, ListName)
    return result

  def FileListItem(self, ListName, Index):
    result = self.dpl.DPLFileListItem(self.instanceID, ListName, Index)
    return result

  def FindFonts(self):
    result = self.dpl.DPLFindFonts(self.instanceID)
    return result

  def FindFormFieldByTitle(self, Title):
    result = self.dpl.DPLFindFormFieldByTitle(self.instanceID, Title)
    return result

  def FindImages(self):
    result = self.dpl.DPLFindImages(self.instanceID)
    return result

  def FitImage(self, Left, Top, Width, Height, HAlign, VAlign, Rotate):
    result = self.dpl.DPLFitImage(self.instanceID, Left, Top, Width, Height, HAlign, VAlign, Rotate)
    return result

  def FitRotatedTextBox(self, Left, Top, Width, Height, Angle, Text, Options):
    result = self.dpl.DPLFitRotatedTextBox(self.instanceID, Left, Top, Width, Height, Angle, Text, Options)
    return result

  def FitTextBox(self, Left, Top, Width, Height, Text, Options):
    result = self.dpl.DPLFitTextBox(self.instanceID, Left, Top, Width, Height, Text, Options)
    return result

  def FlattenAllFormFields(self, Options):
    result = self.dpl.DPLFlattenAllFormFields(self.instanceID, Options)
    return result

  def FlattenAnnot(self, Index, Options):
    result = self.dpl.DPLFlattenAnnot(self.instanceID, Index, Options)
    return result

  def FlattenFormField(self, Index):
    result = self.dpl.DPLFlattenFormField(self.instanceID, Index)
    return result

  def FontCount(self):
    result = self.dpl.DPLFontCount(self.instanceID)
    return result

  def FontFamily(self):
    result = self.dpl.DPLFontFamily(self.instanceID)
    return result

  def FontHasKerning(self):
    result = self.dpl.DPLFontHasKerning(self.instanceID)
    return result

  def FontName(self):
    result = self.dpl.DPLFontName(self.instanceID)
    return result

  def FontReference(self):
    result = self.dpl.DPLFontReference(self.instanceID)
    return result

  def FontSize(self):
    result = self.dpl.DPLFontSize(self.instanceID)
    return result

  def FontType(self):
    result = self.dpl.DPLFontType(self.instanceID)
    return result

  def FormFieldCount(self):
    result = self.dpl.DPLFormFieldCount(self.instanceID)
    return result

  def FormFieldHasParent(self, Index):
    result = self.dpl.DPLFormFieldHasParent(self.instanceID, Index)
    return result

  def FormFieldJavaScriptAction(self, Index, ActionType, JavaScript):
    result = self.dpl.DPLFormFieldJavaScriptAction(self.instanceID, Index, ActionType, JavaScript)
    return result

  def FormFieldWebLinkAction(self, Index, ActionType, Link):
    result = self.dpl.DPLFormFieldWebLinkAction(self.instanceID, Index, ActionType, Link)
    return result

  def GetActionDest(self, ActionID):
    result = self.dpl.DPLGetActionDest(self.instanceID, ActionID)
    return result

  def GetActionType(self, ActionID):
    result = self.dpl.DPLGetActionType(self.instanceID, ActionID)
    return result

  def GetActionURL(self, ActionID):
    result = self.dpl.DPLGetActionURL(self.instanceID, ActionID)
    return result

  def GetAnalysisInfo(self, AnalysisID, AnalysisItem):
    result = self.dpl.DPLGetAnalysisInfo(self.instanceID, AnalysisID, AnalysisItem)
    return result

  def GetAnnotActionID(self, Index):
    result = self.dpl.DPLGetAnnotActionID(self.instanceID, Index)
    return result

  def GetAnnotDblProperty(self, Index, Tag):
    result = self.dpl.DPLGetAnnotDblProperty(self.instanceID, Index, Tag)
    return result

  def GetAnnotDest(self, Index):
    result = self.dpl.DPLGetAnnotDest(self.instanceID, Index)
    return result

  def GetAnnotEmbeddedFileName(self, Index, Options):
    result = self.dpl.DPLGetAnnotEmbeddedFileName(self.instanceID, Index, Options)
    return result

  def GetAnnotEmbeddedFileToFile(self, Index, Options, FileName):
    result = self.dpl.DPLGetAnnotEmbeddedFileToFile(self.instanceID, Index, Options, FileName)
    return result

  def GetAnnotEmbeddedFileToString(self, Index, Options):
    resultPtr = self.dpl.DPLGetAnnotEmbeddedFileToString(self.instanceID, Index, Options)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetAnnotIntProperty(self, Index, Tag):
    result = self.dpl.DPLGetAnnotIntProperty(self.instanceID, Index, Tag)
    return result

  def GetAnnotQuadCount(self, Index):
    result = self.dpl.DPLGetAnnotQuadCount(self.instanceID, Index)
    return result

  def GetAnnotQuadPoints(self, Index, QuadNumber, PointNumber):
    result = self.dpl.DPLGetAnnotQuadPoints(self.instanceID, Index, QuadNumber, PointNumber)
    return result

  def GetAnnotSoundToFile(self, Index, Options, SoundFileName):
    result = self.dpl.DPLGetAnnotSoundToFile(self.instanceID, Index, Options, SoundFileName)
    return result

  def GetAnnotSoundToString(self, Index, Options):
    resultPtr = self.dpl.DPLGetAnnotSoundToString(self.instanceID, Index, Options)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetAnnotStrProperty(self, Index, Tag):
    result = self.dpl.DPLGetAnnotStrProperty(self.instanceID, Index, Tag)
    return result

  def GetBarcodeWidth(self, NominalWidth, Text, Barcode):
    result = self.dpl.DPLGetBarcodeWidth(self.instanceID, NominalWidth, Text, Barcode)
    return result

  def GetBaseURL(self):
    result = self.dpl.DPLGetBaseURL(self.instanceID)
    return result

  def GetCSDictEPSG(self, CSDictID):
    result = self.dpl.DPLGetCSDictEPSG(self.instanceID, CSDictID)
    return result

  def GetCSDictType(self, CSDictID):
    result = self.dpl.DPLGetCSDictType(self.instanceID, CSDictID)
    return result

  def GetCSDictWKT(self, CSDictID):
    result = self.dpl.DPLGetCSDictWKT(self.instanceID, CSDictID)
    return result

  def GetCanvasDC(self, CanvasWidth, CanvasHeight):
    result = self.dpl.DPLGetCanvasDC(self.instanceID, CanvasWidth, CanvasHeight)
    return result

  def GetCanvasDCEx(self, CanvasWidth, CanvasHeight, ReferenceDC):
    result = self.dpl.DPLGetCanvasDCEx(self.instanceID, CanvasWidth, CanvasHeight, ReferenceDC)
    return result

  def GetCatalogInformation(self, Key):
    result = self.dpl.DPLGetCatalogInformation(self.instanceID, Key)
    return result

  def GetContentStreamToString(self):
    resultPtr = self.dpl.DPLGetContentStreamToString(self.instanceID)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetCustomInformation(self, Key):
    result = self.dpl.DPLGetCustomInformation(self.instanceID, Key)
    return result

  def GetCustomKeys(self, Location):
    result = self.dpl.DPLGetCustomKeys(self.instanceID, Location)
    return result

  def GetDefaultPrinterName(self):
    result = self.dpl.DPLGetDefaultPrinterName(self.instanceID)
    return result

  def GetDestName(self, DestID):
    result = self.dpl.DPLGetDestName(self.instanceID, DestID)
    return result

  def GetDestPage(self, DestID):
    result = self.dpl.DPLGetDestPage(self.instanceID, DestID)
    return result

  def GetDestType(self, DestID):
    result = self.dpl.DPLGetDestType(self.instanceID, DestID)
    return result

  def GetDestValue(self, DestID, ValueKey):
    result = self.dpl.DPLGetDestValue(self.instanceID, DestID, ValueKey)
    return result

  def GetDocJavaScript(self, ActionType):
    result = self.dpl.DPLGetDocJavaScript(self.instanceID, ActionType)
    return result

  def GetDocumentFileName(self):
    result = self.dpl.DPLGetDocumentFileName(self.instanceID)
    return result

  def GetDocumentFileSize(self):
    result = self.dpl.DPLGetDocumentFileSize(self.instanceID)
    return result

  def GetDocumentID(self, Index):
    result = self.dpl.DPLGetDocumentID(self.instanceID, Index)
    return result

  def GetDocumentIdentifier(self, Part, Options):
    result = self.dpl.DPLGetDocumentIdentifier(self.instanceID, Part, Options)
    return result

  def GetDocumentMetadata(self):
    result = self.dpl.DPLGetDocumentMetadata(self.instanceID)
    return result

  def GetDocumentRepaired(self):
    result = self.dpl.DPLGetDocumentRepaired(self.instanceID)
    return result

  def GetDocumentResourceList(self):
    result = self.dpl.DPLGetDocumentResourceList(self.instanceID)
    return result

  def GetEmbeddedFileContentToFile(self, Index, FileName):
    result = self.dpl.DPLGetEmbeddedFileContentToFile(self.instanceID, Index, FileName)
    return result

  def GetEmbeddedFileContentToString(self, Index):
    resultPtr = self.dpl.DPLGetEmbeddedFileContentToString(self.instanceID, Index)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetEmbeddedFileID(self, Index):
    result = self.dpl.DPLGetEmbeddedFileID(self.instanceID, Index)
    return result

  def GetEmbeddedFileIntProperty(self, Index, Tag):
    result = self.dpl.DPLGetEmbeddedFileIntProperty(self.instanceID, Index, Tag)
    return result

  def GetEmbeddedFileStrProperty(self, Index, Tag):
    result = self.dpl.DPLGetEmbeddedFileStrProperty(self.instanceID, Index, Tag)
    return result

  def GetEncryptionFingerprint(self):
    result = self.dpl.DPLGetEncryptionFingerprint(self.instanceID)
    return result

  def GetFileMetadata(self, InputFileName, Password):
    result = self.dpl.DPLGetFileMetadata(self.instanceID, InputFileName, Password)
    return result

  def GetFirstChildOutline(self, OutlineID):
    result = self.dpl.DPLGetFirstChildOutline(self.instanceID, OutlineID)
    return result

  def GetFirstOutline(self):
    result = self.dpl.DPLGetFirstOutline(self.instanceID)
    return result

  def GetFontCharacterCodesToString(self, InputText):
    resultPtr = self.dpl.DPLGetFontCharacterCodesToString(self.instanceID, InputText)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetFontEncoding(self):
    result = self.dpl.DPLGetFontEncoding(self.instanceID)
    return result

  def GetFontFlags(self, FontFlagItemID):
    result = self.dpl.DPLGetFontFlags(self.instanceID, FontFlagItemID)
    return result

  def GetFontID(self, Index):
    result = self.dpl.DPLGetFontID(self.instanceID, Index)
    return result

  def GetFontIsEmbedded(self):
    result = self.dpl.DPLGetFontIsEmbedded(self.instanceID)
    return result

  def GetFontIsSubsetted(self):
    result = self.dpl.DPLGetFontIsSubsetted(self.instanceID)
    return result

  def GetFontMetrics(self, MetricType):
    result = self.dpl.DPLGetFontMetrics(self.instanceID, MetricType)
    return result

  def GetFontObjectNumber(self):
    result = self.dpl.DPLGetFontObjectNumber(self.instanceID)
    return result

  def GetFormFieldActionID(self, Index, TriggerEvent):
    result = self.dpl.DPLGetFormFieldActionID(self.instanceID, Index, TriggerEvent)
    return result

  def GetFormFieldAlignment(self, Index):
    result = self.dpl.DPLGetFormFieldAlignment(self.instanceID, Index)
    return result

  def GetFormFieldAnnotFlags(self, Index):
    result = self.dpl.DPLGetFormFieldAnnotFlags(self.instanceID, Index)
    return result

  def GetFormFieldBackgroundColor(self, Index, ColorComponent):
    result = self.dpl.DPLGetFormFieldBackgroundColor(self.instanceID, Index, ColorComponent)
    return result

  def GetFormFieldBackgroundColorType(self, Index):
    result = self.dpl.DPLGetFormFieldBackgroundColorType(self.instanceID, Index)
    return result

  def GetFormFieldBorderColor(self, Index, ColorComponent):
    result = self.dpl.DPLGetFormFieldBorderColor(self.instanceID, Index, ColorComponent)
    return result

  def GetFormFieldBorderColorType(self, Index):
    result = self.dpl.DPLGetFormFieldBorderColorType(self.instanceID, Index)
    return result

  def GetFormFieldBorderProperty(self, Index, PropKey):
    result = self.dpl.DPLGetFormFieldBorderProperty(self.instanceID, Index, PropKey)
    return result

  def GetFormFieldBorderStyle(self, Index):
    result = self.dpl.DPLGetFormFieldBorderStyle(self.instanceID, Index)
    return result

  def GetFormFieldBound(self, Index, Edge):
    result = self.dpl.DPLGetFormFieldBound(self.instanceID, Index, Edge)
    return result

  def GetFormFieldCaption(self, Index):
    result = self.dpl.DPLGetFormFieldCaption(self.instanceID, Index)
    return result

  def GetFormFieldCaptionEx(self, Index, StringType):
    result = self.dpl.DPLGetFormFieldCaptionEx(self.instanceID, Index, StringType)
    return result

  def GetFormFieldCheckStyle(self, Index):
    result = self.dpl.DPLGetFormFieldCheckStyle(self.instanceID, Index)
    return result

  def GetFormFieldChildTitle(self, Index):
    result = self.dpl.DPLGetFormFieldChildTitle(self.instanceID, Index)
    return result

  def GetFormFieldChoiceType(self, Index):
    result = self.dpl.DPLGetFormFieldChoiceType(self.instanceID, Index)
    return result

  def GetFormFieldColor(self, Index, ColorComponent):
    result = self.dpl.DPLGetFormFieldColor(self.instanceID, Index, ColorComponent)
    return result

  def GetFormFieldComb(self, Index):
    result = self.dpl.DPLGetFormFieldComb(self.instanceID, Index)
    return result

  def GetFormFieldDefaultValue(self, Index):
    result = self.dpl.DPLGetFormFieldDefaultValue(self.instanceID, Index)
    return result

  def GetFormFieldDescription(self, Index):
    result = self.dpl.DPLGetFormFieldDescription(self.instanceID, Index)
    return result

  def GetFormFieldFlags(self, Index):
    result = self.dpl.DPLGetFormFieldFlags(self.instanceID, Index)
    return result

  def GetFormFieldFontName(self, Index):
    result = self.dpl.DPLGetFormFieldFontName(self.instanceID, Index)
    return result

  def GetFormFieldJavaScript(self, Index, ActionType):
    result = self.dpl.DPLGetFormFieldJavaScript(self.instanceID, Index, ActionType)
    return result

  def GetFormFieldKidCount(self, Index):
    result = self.dpl.DPLGetFormFieldKidCount(self.instanceID, Index)
    return result

  def GetFormFieldKidTempIndex(self, Index, SubIndex):
    result = self.dpl.DPLGetFormFieldKidTempIndex(self.instanceID, Index, SubIndex)
    return result

  def GetFormFieldMaxLen(self, Index):
    result = self.dpl.DPLGetFormFieldMaxLen(self.instanceID, Index)
    return result

  def GetFormFieldNoExport(self, Index):
    result = self.dpl.DPLGetFormFieldNoExport(self.instanceID, Index)
    return result

  def GetFormFieldPage(self, Index):
    result = self.dpl.DPLGetFormFieldPage(self.instanceID, Index)
    return result

  def GetFormFieldPrintable(self, Index):
    result = self.dpl.DPLGetFormFieldPrintable(self.instanceID, Index)
    return result

  def GetFormFieldReadOnly(self, Index):
    result = self.dpl.DPLGetFormFieldReadOnly(self.instanceID, Index)
    return result

  def GetFormFieldRequired(self, Index):
    result = self.dpl.DPLGetFormFieldRequired(self.instanceID, Index)
    return result

  def GetFormFieldRichTextString(self, Index, Key):
    result = self.dpl.DPLGetFormFieldRichTextString(self.instanceID, Index, Key)
    return result

  def GetFormFieldRotation(self, Index):
    result = self.dpl.DPLGetFormFieldRotation(self.instanceID, Index)
    return result

  def GetFormFieldSubCount(self, Index):
    result = self.dpl.DPLGetFormFieldSubCount(self.instanceID, Index)
    return result

  def GetFormFieldSubDisplayName(self, Index, SubIndex):
    result = self.dpl.DPLGetFormFieldSubDisplayName(self.instanceID, Index, SubIndex)
    return result

  def GetFormFieldSubName(self, Index, SubIndex):
    result = self.dpl.DPLGetFormFieldSubName(self.instanceID, Index, SubIndex)
    return result

  def GetFormFieldSubmitActionString(self, Index, ActionType):
    result = self.dpl.DPLGetFormFieldSubmitActionString(self.instanceID, Index, ActionType)
    return result

  def GetFormFieldTabOrder(self, Index):
    result = self.dpl.DPLGetFormFieldTabOrder(self.instanceID, Index)
    return result

  def GetFormFieldTabOrderEx(self, Index, Options):
    result = self.dpl.DPLGetFormFieldTabOrderEx(self.instanceID, Index, Options)
    return result

  def GetFormFieldTextFlags(self, Index, ValueKey):
    result = self.dpl.DPLGetFormFieldTextFlags(self.instanceID, Index, ValueKey)
    return result

  def GetFormFieldTextSize(self, Index):
    result = self.dpl.DPLGetFormFieldTextSize(self.instanceID, Index)
    return result

  def GetFormFieldTitle(self, Index):
    result = self.dpl.DPLGetFormFieldTitle(self.instanceID, Index)
    return result

  def GetFormFieldType(self, Index):
    result = self.dpl.DPLGetFormFieldType(self.instanceID, Index)
    return result

  def GetFormFieldValue(self, Index):
    result = self.dpl.DPLGetFormFieldValue(self.instanceID, Index)
    return result

  def GetFormFieldValueByTitle(self, Title):
    result = self.dpl.DPLGetFormFieldValueByTitle(self.instanceID, Title)
    return result

  def GetFormFieldVisible(self, Index):
    result = self.dpl.DPLGetFormFieldVisible(self.instanceID, Index)
    return result

  def GetFormFieldWebLink(self, Index, ActionType):
    result = self.dpl.DPLGetFormFieldWebLink(self.instanceID, Index, ActionType)
    return result

  def GetFormFontCount(self):
    result = self.dpl.DPLGetFormFontCount(self.instanceID)
    return result

  def GetFormFontName(self, FontIndex):
    result = self.dpl.DPLGetFormFontName(self.instanceID, FontIndex)
    return result

  def GetGlobalJavaScript(self, PackageName):
    result = self.dpl.DPLGetGlobalJavaScript(self.instanceID, PackageName)
    return result

  def GetHTMLTextHeight(self, Width, HTMLText):
    result = self.dpl.DPLGetHTMLTextHeight(self.instanceID, Width, HTMLText)
    return result

  def GetHTMLTextLineCount(self, Width, HTMLText):
    result = self.dpl.DPLGetHTMLTextLineCount(self.instanceID, Width, HTMLText)
    return result

  def GetHTMLTextWidth(self, MaxWidth, HTMLText):
    result = self.dpl.DPLGetHTMLTextWidth(self.instanceID, MaxWidth, HTMLText)
    return result

  def GetImageID(self, Index):
    result = self.dpl.DPLGetImageID(self.instanceID, Index)
    return result

  def GetImageListCount(self, ImageListID):
    result = self.dpl.DPLGetImageListCount(self.instanceID, ImageListID)
    return result

  def GetImageListItemDataToString(self, ImageListID, ImageIndex, Options):
    resultPtr = self.dpl.DPLGetImageListItemDataToString(self.instanceID, ImageListID, ImageIndex, Options)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetImageListItemDblProperty(self, ImageListID, ImageIndex, PropertyID):
    result = self.dpl.DPLGetImageListItemDblProperty(self.instanceID, ImageListID, ImageIndex, PropertyID)
    return result

  def GetImageListItemFormatDesc(self, ImageListID, ImageIndex, Options):
    result = self.dpl.DPLGetImageListItemFormatDesc(self.instanceID, ImageListID, ImageIndex, Options)
    return result

  def GetImageListItemIntProperty(self, ImageListID, ImageIndex, PropertyID):
    result = self.dpl.DPLGetImageListItemIntProperty(self.instanceID, ImageListID, ImageIndex, PropertyID)
    return result

  def GetImageMeasureDict(self):
    result = self.dpl.DPLGetImageMeasureDict(self.instanceID)
    return result

  def GetImagePageCount(self, FileName):
    result = self.dpl.DPLGetImagePageCount(self.instanceID, FileName)
    return result

  def GetImagePageCountFromString(self, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLGetImagePageCountFromString(self.instanceID, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def GetImagePtDataDict(self):
    result = self.dpl.DPLGetImagePtDataDict(self.instanceID)
    return result

  def GetInformation(self, Key):
    result = self.dpl.DPLGetInformation(self.instanceID, Key)
    return result

  def GetInstalledFontsByCharset(self, CharsetIndex, Options):
    result = self.dpl.DPLGetInstalledFontsByCharset(self.instanceID, CharsetIndex, Options)
    return result

  def GetInstalledFontsByCodePage(self, CodePage, Options):
    result = self.dpl.DPLGetInstalledFontsByCodePage(self.instanceID, CodePage, Options)
    return result

  def GetKerning(self, CharPair):
    result = self.dpl.DPLGetKerning(self.instanceID, CharPair)
    return result

  def GetLatestPrinterNames(self):
    result = self.dpl.DPLGetLatestPrinterNames(self.instanceID)
    return result

  def GetMaxObjectNumber(self):
    result = self.dpl.DPLGetMaxObjectNumber(self.instanceID)
    return result

  def GetMeasureDictBoundsCount(self, MeasureDictID):
    result = self.dpl.DPLGetMeasureDictBoundsCount(self.instanceID, MeasureDictID)
    return result

  def GetMeasureDictBoundsItem(self, MeasureDictID, ItemIndex):
    result = self.dpl.DPLGetMeasureDictBoundsItem(self.instanceID, MeasureDictID, ItemIndex)
    return result

  def GetMeasureDictCoordinateSystem(self, MeasureDictID):
    result = self.dpl.DPLGetMeasureDictCoordinateSystem(self.instanceID, MeasureDictID)
    return result

  def GetMeasureDictDCSDict(self, MeasureDictID):
    result = self.dpl.DPLGetMeasureDictDCSDict(self.instanceID, MeasureDictID)
    return result

  def GetMeasureDictGCSDict(self, MeasureDictID):
    result = self.dpl.DPLGetMeasureDictGCSDict(self.instanceID, MeasureDictID)
    return result

  def GetMeasureDictGPTSCount(self, MeasureDictID):
    result = self.dpl.DPLGetMeasureDictGPTSCount(self.instanceID, MeasureDictID)
    return result

  def GetMeasureDictGPTSItem(self, MeasureDictID, ItemIndex):
    result = self.dpl.DPLGetMeasureDictGPTSItem(self.instanceID, MeasureDictID, ItemIndex)
    return result

  def GetMeasureDictLPTSCount(self, MeasureDictID):
    result = self.dpl.DPLGetMeasureDictLPTSCount(self.instanceID, MeasureDictID)
    return result

  def GetMeasureDictLPTSItem(self, MeasureDictID, ItemIndex):
    result = self.dpl.DPLGetMeasureDictLPTSItem(self.instanceID, MeasureDictID, ItemIndex)
    return result

  def GetMeasureDictPDU(self, MeasureDictID, UnitIndex):
    result = self.dpl.DPLGetMeasureDictPDU(self.instanceID, MeasureDictID, UnitIndex)
    return result

  def GetNamedDestination(self, DestName):
    result = self.dpl.DPLGetNamedDestination(self.instanceID, DestName)
    return result

  def GetNeedAppearances(self):
    result = self.dpl.DPLGetNeedAppearances(self.instanceID)
    return result

  def GetNextOutline(self, OutlineID):
    result = self.dpl.DPLGetNextOutline(self.instanceID, OutlineID)
    return result

  def GetObjectCount(self):
    result = self.dpl.DPLGetObjectCount(self.instanceID)
    return result

  def GetObjectDecodeError(self, ObjectNumber):
    result = self.dpl.DPLGetObjectDecodeError(self.instanceID, ObjectNumber)
    return result

  def GetObjectToString(self, ObjectNumber):
    resultPtr = self.dpl.DPLGetObjectToString(self.instanceID, ObjectNumber)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetOpenActionDestination(self):
    result = self.dpl.DPLGetOpenActionDestination(self.instanceID)
    return result

  def GetOpenActionJavaScript(self):
    result = self.dpl.DPLGetOpenActionJavaScript(self.instanceID)
    return result

  def GetOptionalContentConfigCount(self):
    result = self.dpl.DPLGetOptionalContentConfigCount(self.instanceID)
    return result

  def GetOptionalContentConfigLocked(self, OptionalContentConfigID, OptionalContentGroupID):
    result = self.dpl.DPLGetOptionalContentConfigLocked(self.instanceID, OptionalContentConfigID, OptionalContentGroupID)
    return result

  def GetOptionalContentConfigOrderCount(self, OptionalContentConfigID):
    result = self.dpl.DPLGetOptionalContentConfigOrderCount(self.instanceID, OptionalContentConfigID)
    return result

  def GetOptionalContentConfigOrderItemID(self, OptionalContentConfigID, ItemIndex):
    result = self.dpl.DPLGetOptionalContentConfigOrderItemID(self.instanceID, OptionalContentConfigID, ItemIndex)
    return result

  def GetOptionalContentConfigOrderItemLabel(self, OptionalContentConfigID, ItemIndex):
    result = self.dpl.DPLGetOptionalContentConfigOrderItemLabel(self.instanceID, OptionalContentConfigID, ItemIndex)
    return result

  def GetOptionalContentConfigOrderItemLevel(self, OptionalContentConfigID, ItemIndex):
    result = self.dpl.DPLGetOptionalContentConfigOrderItemLevel(self.instanceID, OptionalContentConfigID, ItemIndex)
    return result

  def GetOptionalContentConfigOrderItemType(self, OptionalContentConfigID, ItemIndex):
    result = self.dpl.DPLGetOptionalContentConfigOrderItemType(self.instanceID, OptionalContentConfigID, ItemIndex)
    return result

  def GetOptionalContentConfigState(self, OptionalContentConfigID, OptionalContentGroupID):
    result = self.dpl.DPLGetOptionalContentConfigState(self.instanceID, OptionalContentConfigID, OptionalContentGroupID)
    return result

  def GetOptionalContentGroupID(self, Index):
    result = self.dpl.DPLGetOptionalContentGroupID(self.instanceID, Index)
    return result

  def GetOptionalContentGroupName(self, OptionalContentGroupID):
    result = self.dpl.DPLGetOptionalContentGroupName(self.instanceID, OptionalContentGroupID)
    return result

  def GetOptionalContentGroupPrintable(self, OptionalContentGroupID):
    result = self.dpl.DPLGetOptionalContentGroupPrintable(self.instanceID, OptionalContentGroupID)
    return result

  def GetOptionalContentGroupVisible(self, OptionalContentGroupID):
    result = self.dpl.DPLGetOptionalContentGroupVisible(self.instanceID, OptionalContentGroupID)
    return result

  def GetOrigin(self):
    result = self.dpl.DPLGetOrigin(self.instanceID)
    return result

  def GetOutlineActionID(self, OutlineID):
    result = self.dpl.DPLGetOutlineActionID(self.instanceID, OutlineID)
    return result

  def GetOutlineColor(self, OutlineID, ColorComponent):
    result = self.dpl.DPLGetOutlineColor(self.instanceID, OutlineID, ColorComponent)
    return result

  def GetOutlineDest(self, OutlineID):
    result = self.dpl.DPLGetOutlineDest(self.instanceID, OutlineID)
    return result

  def GetOutlineID(self, Index):
    result = self.dpl.DPLGetOutlineID(self.instanceID, Index)
    return result

  def GetOutlineJavaScript(self, OutlineID):
    result = self.dpl.DPLGetOutlineJavaScript(self.instanceID, OutlineID)
    return result

  def GetOutlineObjectNumber(self, OutlineID):
    result = self.dpl.DPLGetOutlineObjectNumber(self.instanceID, OutlineID)
    return result

  def GetOutlineOpenFile(self, OutlineID):
    result = self.dpl.DPLGetOutlineOpenFile(self.instanceID, OutlineID)
    return result

  def GetOutlinePage(self, OutlineID):
    result = self.dpl.DPLGetOutlinePage(self.instanceID, OutlineID)
    return result

  def GetOutlineStyle(self, OutlineID):
    result = self.dpl.DPLGetOutlineStyle(self.instanceID, OutlineID)
    return result

  def GetOutlineWebLink(self, OutlineID):
    result = self.dpl.DPLGetOutlineWebLink(self.instanceID, OutlineID)
    return result

  def GetPDF417SymbolHeight(self, Text, Options, FixedColumns, FixedRows, ErrorLevel, ModuleSize, HeightWidthRatio):
    result = self.dpl.DPLGetPDF417SymbolHeight(self.instanceID, Text, Options, FixedColumns, FixedRows, ErrorLevel, ModuleSize, HeightWidthRatio)
    return result

  def GetPDF417SymbolWidth(self, Text, Options, FixedColumns, FixedRows, ErrorLevel, ModuleSize, HeightWidthRatio):
    result = self.dpl.DPLGetPDF417SymbolWidth(self.instanceID, Text, Options, FixedColumns, FixedRows, ErrorLevel, ModuleSize, HeightWidthRatio)
    return result

  def GetPageBox(self, BoxType, Dimension):
    result = self.dpl.DPLGetPageBox(self.instanceID, BoxType, Dimension)
    return result

  def GetPageColorSpaces(self, Options):
    result = self.dpl.DPLGetPageColorSpaces(self.instanceID, Options)
    return result

  def GetPageContentToString(self):
    resultPtr = self.dpl.DPLGetPageContentToString(self.instanceID)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetPageImageList(self, Options):
    result = self.dpl.DPLGetPageImageList(self.instanceID, Options)
    return result

  def GetPageJavaScript(self, ActionType):
    result = self.dpl.DPLGetPageJavaScript(self.instanceID, ActionType)
    return result

  def GetPageLGIDictContent(self, DictIndex):
    result = self.dpl.DPLGetPageLGIDictContent(self.instanceID, DictIndex)
    return result

  def GetPageLGIDictCount(self):
    result = self.dpl.DPLGetPageLGIDictCount(self.instanceID)
    return result

  def GetPageLabel(self, Page):
    result = self.dpl.DPLGetPageLabel(self.instanceID, Page)
    return result

  def GetPageLayout(self):
    result = self.dpl.DPLGetPageLayout(self.instanceID)
    return result

  def GetPageMetricsToString(self, StartPage, EndPage, Options):
    resultPtr = self.dpl.DPLGetPageMetricsToString(self.instanceID, StartPage, EndPage, Options)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetPageMode(self):
    result = self.dpl.DPLGetPageMode(self.instanceID)
    return result

  def GetPageText(self, ExtractOptions):
    result = self.dpl.DPLGetPageText(self.instanceID, ExtractOptions)
    return result

  def GetPageUserUnit(self):
    result = self.dpl.DPLGetPageUserUnit(self.instanceID)
    return result

  def GetPageViewPortCount(self):
    result = self.dpl.DPLGetPageViewPortCount(self.instanceID)
    return result

  def GetPageViewPortID(self, Index):
    result = self.dpl.DPLGetPageViewPortID(self.instanceID, Index)
    return result

  def GetParentOutline(self, OutlineID):
    result = self.dpl.DPLGetParentOutline(self.instanceID, OutlineID)
    return result

  def GetPrevOutline(self, OutlineID):
    result = self.dpl.DPLGetPrevOutline(self.instanceID, OutlineID)
    return result

  def GetPrintPreviewBitmapToString(self, PrinterName, PreviewPage, PrintOptions, MaxDimension, PreviewOptions):
    resultPtr = self.dpl.DPLGetPrintPreviewBitmapToString(self.instanceID, PrinterName, PreviewPage, PrintOptions, MaxDimension, PreviewOptions)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetPrinterBins(self, PrinterName):
    result = self.dpl.DPLGetPrinterBins(self.instanceID, PrinterName)
    return result

  def GetPrinterDevModeToString(self, PrinterName):
    resultPtr = self.dpl.DPLGetPrinterDevModeToString(self.instanceID, PrinterName)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GetPrinterMediaTypes(self, PrinterName):
    result = self.dpl.DPLGetPrinterMediaTypes(self.instanceID, PrinterName)
    return result

  def GetPrinterNames(self):
    result = self.dpl.DPLGetPrinterNames(self.instanceID)
    return result

  def GetRenderScale(self):
    result = self.dpl.DPLGetRenderScale(self.instanceID)
    return result

  def GetScale(self):
    result = self.dpl.DPLGetScale(self.instanceID)
    return result

  def GetSignProcessByteRange(self, SignProcessID, ArrayPosition):
    result = self.dpl.DPLGetSignProcessByteRange(self.instanceID, SignProcessID, ArrayPosition)
    return result

  def GetSignProcessResult(self, SignProcessID):
    result = self.dpl.DPLGetSignProcessResult(self.instanceID, SignProcessID)
    return result

  def GetStringListCount(self, StringListID):
    result = self.dpl.DPLGetStringListCount(self.instanceID, StringListID)
    return result

  def GetStringListItem(self, StringListID, ItemIndex):
    result = self.dpl.DPLGetStringListItem(self.instanceID, StringListID, ItemIndex)
    return result

  def GetTabOrderMode(self):
    result = self.dpl.DPLGetTabOrderMode(self.instanceID)
    return result

  def GetTableCellDblProperty(self, TableID, RowNumber, ColumnNumber, Tag):
    result = self.dpl.DPLGetTableCellDblProperty(self.instanceID, TableID, RowNumber, ColumnNumber, Tag)
    return result

  def GetTableCellIntProperty(self, TableID, RowNumber, ColumnNumber, Tag):
    result = self.dpl.DPLGetTableCellIntProperty(self.instanceID, TableID, RowNumber, ColumnNumber, Tag)
    return result

  def GetTableCellStrProperty(self, TableID, RowNumber, ColumnNumber, Tag):
    result = self.dpl.DPLGetTableCellStrProperty(self.instanceID, TableID, RowNumber, ColumnNumber, Tag)
    return result

  def GetTableColumnCount(self, TableID):
    result = self.dpl.DPLGetTableColumnCount(self.instanceID, TableID)
    return result

  def GetTableLastDrawnRow(self, TableID):
    result = self.dpl.DPLGetTableLastDrawnRow(self.instanceID, TableID)
    return result

  def GetTableRowCount(self, TableID):
    result = self.dpl.DPLGetTableRowCount(self.instanceID, TableID)
    return result

  def GetTempPath(self):
    result = self.dpl.DPLGetTempPath(self.instanceID)
    return result

  def GetTextAscent(self):
    result = self.dpl.DPLGetTextAscent(self.instanceID)
    return result

  def GetTextBlockAsString(self, TextBlockListID, Index):
    result = self.dpl.DPLGetTextBlockAsString(self.instanceID, TextBlockListID, Index)
    return result

  def GetTextBlockBound(self, TextBlockListID, Index, BoundIndex):
    result = self.dpl.DPLGetTextBlockBound(self.instanceID, TextBlockListID, Index, BoundIndex)
    return result

  def GetTextBlockCharWidth(self, TextBlockListID, Index, CharIndex):
    result = self.dpl.DPLGetTextBlockCharWidth(self.instanceID, TextBlockListID, Index, CharIndex)
    return result

  def GetTextBlockColor(self, TextBlockListID, Index, ColorComponent):
    result = self.dpl.DPLGetTextBlockColor(self.instanceID, TextBlockListID, Index, ColorComponent)
    return result

  def GetTextBlockColorType(self, TextBlockListID, Index):
    result = self.dpl.DPLGetTextBlockColorType(self.instanceID, TextBlockListID, Index)
    return result

  def GetTextBlockCount(self, TextBlockListID):
    result = self.dpl.DPLGetTextBlockCount(self.instanceID, TextBlockListID)
    return result

  def GetTextBlockFontName(self, TextBlockListID, Index):
    result = self.dpl.DPLGetTextBlockFontName(self.instanceID, TextBlockListID, Index)
    return result

  def GetTextBlockFontSize(self, TextBlockListID, Index):
    result = self.dpl.DPLGetTextBlockFontSize(self.instanceID, TextBlockListID, Index)
    return result

  def GetTextBlockText(self, TextBlockListID, Index):
    result = self.dpl.DPLGetTextBlockText(self.instanceID, TextBlockListID, Index)
    return result

  def GetTextBound(self, Edge):
    result = self.dpl.DPLGetTextBound(self.instanceID, Edge)
    return result

  def GetTextDescent(self):
    result = self.dpl.DPLGetTextDescent(self.instanceID)
    return result

  def GetTextHeight(self):
    result = self.dpl.DPLGetTextHeight(self.instanceID)
    return result

  def GetTextSize(self):
    result = self.dpl.DPLGetTextSize(self.instanceID)
    return result

  def GetTextWidth(self, Text):
    result = self.dpl.DPLGetTextWidth(self.instanceID, Text)
    return result

  def GetUnicodeCharactersFromEncoding(self, Encoding):
    result = self.dpl.DPLGetUnicodeCharactersFromEncoding(self.instanceID, Encoding)
    return result

  def GetViewPortBBox(self, ViewPortID, Dimension):
    result = self.dpl.DPLGetViewPortBBox(self.instanceID, ViewPortID, Dimension)
    return result

  def GetViewPortMeasureDict(self, ViewPortID):
    result = self.dpl.DPLGetViewPortMeasureDict(self.instanceID, ViewPortID)
    return result

  def GetViewPortName(self, ViewPortID):
    result = self.dpl.DPLGetViewPortName(self.instanceID, ViewPortID)
    return result

  def GetViewPortPtDataDict(self, ViewPortID):
    result = self.dpl.DPLGetViewPortPtDataDict(self.instanceID, ViewPortID)
    return result

  def GetViewerPreferences(self, Option):
    result = self.dpl.DPLGetViewerPreferences(self.instanceID, Option)
    return result

  def GetWrappedText(self, Width, Delimiter, Text):
    result = self.dpl.DPLGetWrappedText(self.instanceID, Width, Delimiter, Text)
    return result

  def GetWrappedTextBreakString(self, Width, Delimiter, Text):
    result = self.dpl.DPLGetWrappedTextBreakString(self.instanceID, Width, Delimiter, Text)
    return result

  def GetWrappedTextHeight(self, Width, Text):
    result = self.dpl.DPLGetWrappedTextHeight(self.instanceID, Width, Text)
    return result

  def GetWrappedTextLineCount(self, Width, Text):
    result = self.dpl.DPLGetWrappedTextLineCount(self.instanceID, Width, Text)
    return result

  def GetXFAFormFieldCount(self):
    result = self.dpl.DPLGetXFAFormFieldCount(self.instanceID)
    return result

  def GetXFAFormFieldName(self, Index):
    result = self.dpl.DPLGetXFAFormFieldName(self.instanceID, Index)
    return result

  def GetXFAFormFieldNames(self, Delimiter):
    result = self.dpl.DPLGetXFAFormFieldNames(self.instanceID, Delimiter)
    return result

  def GetXFAFormFieldValue(self, XFAFieldName):
    result = self.dpl.DPLGetXFAFormFieldValue(self.instanceID, XFAFieldName)
    return result

  def GetXFAToString(self, Options):
    resultPtr = self.dpl.DPLGetXFAToString(self.instanceID, Options)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def GlobalJavaScriptCount(self):
    result = self.dpl.DPLGlobalJavaScriptCount(self.instanceID)
    return result

  def GlobalJavaScriptPackageName(self, Index):
    result = self.dpl.DPLGlobalJavaScriptPackageName(self.instanceID, Index)
    return result

  def HasFontResources(self):
    result = self.dpl.DPLHasFontResources(self.instanceID)
    return result

  def HasPageBox(self, BoxType):
    result = self.dpl.DPLHasPageBox(self.instanceID, BoxType)
    return result

  def HidePage(self):
    result = self.dpl.DPLHidePage(self.instanceID)
    return result

  def ImageCount(self):
    result = self.dpl.DPLImageCount(self.instanceID)
    return result

  def ImageFillColor(self):
    result = self.dpl.DPLImageFillColor(self.instanceID)
    return result

  def ImageHeight(self):
    result = self.dpl.DPLImageHeight(self.instanceID)
    return result

  def ImageHorizontalResolution(self):
    result = self.dpl.DPLImageHorizontalResolution(self.instanceID)
    return result

  def ImageResolutionUnits(self):
    result = self.dpl.DPLImageResolutionUnits(self.instanceID)
    return result

  def ImageType(self):
    result = self.dpl.DPLImageType(self.instanceID)
    return result

  def ImageVerticalResolution(self):
    result = self.dpl.DPLImageVerticalResolution(self.instanceID)
    return result

  def ImageWidth(self):
    result = self.dpl.DPLImageWidth(self.instanceID)
    return result

  def ImportEMFFromFile(self, FileName, FontOptions, GeneralOptions):
    result = self.dpl.DPLImportEMFFromFile(self.instanceID, FileName, FontOptions, GeneralOptions)
    return result

  def InsertPages(self, StartPage, PageCount):
    result = self.dpl.DPLInsertPages(self.instanceID, StartPage, PageCount)
    return result

  def InsertTableColumns(self, TableID, Position, NewColumnCount):
    result = self.dpl.DPLInsertTableColumns(self.instanceID, TableID, Position, NewColumnCount)
    return result

  def InsertTableRows(self, TableID, Position, NewRowCount):
    result = self.dpl.DPLInsertTableRows(self.instanceID, TableID, Position, NewRowCount)
    return result

  def IsAnnotFormField(self, Index):
    result = self.dpl.DPLIsAnnotFormField(self.instanceID, Index)
    return result

  def IsLinearized(self):
    result = self.dpl.DPLIsLinearized(self.instanceID)
    return result

  def IsTaggedPDF(self):
    result = self.dpl.DPLIsTaggedPDF(self.instanceID)
    return result

  def LastErrorCode(self):
    result = self.dpl.DPLLastErrorCode(self.instanceID)
    return result

  def LastRenderError(self):
    result = self.dpl.DPLLastRenderError(self.instanceID)
    return result

  def LibraryVersion(self):
    result = self.dpl.DPLLibraryVersion(self.instanceID)
    return result

  def LibraryVersionEx(self):
    result = self.dpl.DPLLibraryVersionEx(self.instanceID)
    return result

  def LicenseInfo(self):
    result = self.dpl.DPLLicenseInfo(self.instanceID)
    return result

  def LinearizeFile(self, InputFileName, Password, OutputFileName, Options):
    result = self.dpl.DPLLinearizeFile(self.instanceID, InputFileName, Password, OutputFileName, Options)
    return result

  def LoadFromCanvasDC(self, DPI, Options):
    result = self.dpl.DPLLoadFromCanvasDC(self.instanceID, DPI, Options)
    return result

  def LoadFromFile(self, FileName, Password):
    result = self.dpl.DPLLoadFromFile(self.instanceID, FileName, Password)
    return result

  def LoadFromString(self, Source, Password):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLLoadFromString(self.instanceID, SourceBuffer, Password)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def LoadState(self):
    result = self.dpl.DPLLoadState(self.instanceID)
    return result

  def MergeDocument(self, DocumentID):
    result = self.dpl.DPLMergeDocument(self.instanceID, DocumentID)
    return result

  def MergeFileList(self, ListName, OutputFileName):
    result = self.dpl.DPLMergeFileList(self.instanceID, ListName, OutputFileName)
    return result

  def MergeFileListFast(self, ListName, OutputFileName):
    result = self.dpl.DPLMergeFileListFast(self.instanceID, ListName, OutputFileName)
    return result

  def MergeFiles(self, FirstFileName, SecondFileName, OutputFileName):
    result = self.dpl.DPLMergeFiles(self.instanceID, FirstFileName, SecondFileName, OutputFileName)
    return result

  def MergeTableCells(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn):
    result = self.dpl.DPLMergeTableCells(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn)
    return result

  def MoveContentStream(self, FromPosition, ToPosition):
    result = self.dpl.DPLMoveContentStream(self.instanceID, FromPosition, ToPosition)
    return result

  def MoveOutlineAfter(self, OutlineID, SiblingID):
    result = self.dpl.DPLMoveOutlineAfter(self.instanceID, OutlineID, SiblingID)
    return result

  def MoveOutlineBefore(self, OutlineID, SiblingID):
    result = self.dpl.DPLMoveOutlineBefore(self.instanceID, OutlineID, SiblingID)
    return result

  def MovePage(self, NewPosition):
    result = self.dpl.DPLMovePage(self.instanceID, NewPosition)
    return result

  def MovePath(self, NewX, NewY):
    result = self.dpl.DPLMovePath(self.instanceID, NewX, NewY)
    return result

  def MultiplyScale(self, MultScaleBy):
    result = self.dpl.DPLMultiplyScale(self.instanceID, MultScaleBy)
    return result

  def NewCMYKAxialShader(self, ShaderName, StartX, StartY, StartCyan, StartMagenta, StartYellow, StartBlack, EndX, EndY, EndCyan, EndMagenta, EndYellow, EndBlack, Extend):
    result = self.dpl.DPLNewCMYKAxialShader(self.instanceID, ShaderName, StartX, StartY, StartCyan, StartMagenta, StartYellow, StartBlack, EndX, EndY, EndCyan, EndMagenta, EndYellow, EndBlack, Extend)
    return result

  def NewChildFormField(self, Index, Title, FieldType):
    result = self.dpl.DPLNewChildFormField(self.instanceID, Index, Title, FieldType)
    return result

  def NewContentStream(self):
    result = self.dpl.DPLNewContentStream(self.instanceID)
    return result

  def NewCustomPrinter(self, OriginalPrinterName):
    result = self.dpl.DPLNewCustomPrinter(self.instanceID, OriginalPrinterName)
    return result

  def NewDestination(self, DestPage, Zoom, DestType, Left, Top, Right, Bottom):
    result = self.dpl.DPLNewDestination(self.instanceID, DestPage, Zoom, DestType, Left, Top, Right, Bottom)
    return result

  def NewDocument(self):
    result = self.dpl.DPLNewDocument(self.instanceID)
    return result

  def NewFormField(self, Title, FieldType):
    result = self.dpl.DPLNewFormField(self.instanceID, Title, FieldType)
    return result

  def NewInternalPrinterObject(self, Options):
    result = self.dpl.DPLNewInternalPrinterObject(self.instanceID, Options)
    return result

  def NewNamedDestination(self, DestName, DestID):
    result = self.dpl.DPLNewNamedDestination(self.instanceID, DestName, DestID)
    return result

  def NewOptionalContentGroup(self, GroupName):
    result = self.dpl.DPLNewOptionalContentGroup(self.instanceID, GroupName)
    return result

  def NewOutline(self, Parent, Title, DestPage, DestPosition):
    result = self.dpl.DPLNewOutline(self.instanceID, Parent, Title, DestPage, DestPosition)
    return result

  def NewPage(self):
    result = self.dpl.DPLNewPage(self.instanceID)
    return result

  def NewPageFromCanvasDC(self, DPI, Options):
    result = self.dpl.DPLNewPageFromCanvasDC(self.instanceID, DPI, Options)
    return result

  def NewPages(self, PageCount):
    result = self.dpl.DPLNewPages(self.instanceID, PageCount)
    return result

  def NewPostScriptXObject(self, PS):
    result = self.dpl.DPLNewPostScriptXObject(self.instanceID, PS)
    return result

  def NewRGBAxialShader(self, ShaderName, StartX, StartY, StartRed, StartGreen, StartBlue, EndX, EndY, EndRed, EndGreen, EndBlue, Extend):
    result = self.dpl.DPLNewRGBAxialShader(self.instanceID, ShaderName, StartX, StartY, StartRed, StartGreen, StartBlue, EndX, EndY, EndRed, EndGreen, EndBlue, Extend)
    return result

  def NewSignProcessFromFile(self, InputFile, Password):
    result = self.dpl.DPLNewSignProcessFromFile(self.instanceID, InputFile, Password)
    return result

  def NewSignProcessFromString(self, Source, Password):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLNewSignProcessFromString(self.instanceID, SourceBuffer, Password)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def NewStaticOutline(self, Parent, Title):
    result = self.dpl.DPLNewStaticOutline(self.instanceID, Parent, Title)
    return result

  def NewTilingPatternFromCapturedPage(self, PatternName, CaptureID):
    result = self.dpl.DPLNewTilingPatternFromCapturedPage(self.instanceID, PatternName, CaptureID)
    return result

  def NoEmbedFontListAdd(self, FontName):
    result = self.dpl.DPLNoEmbedFontListAdd(self.instanceID, FontName)
    return result

  def NoEmbedFontListCount(self):
    result = self.dpl.DPLNoEmbedFontListCount(self.instanceID)
    return result

  def NoEmbedFontListGet(self, Index):
    result = self.dpl.DPLNoEmbedFontListGet(self.instanceID, Index)
    return result

  def NoEmbedFontListRemoveAll(self):
    result = self.dpl.DPLNoEmbedFontListRemoveAll(self.instanceID)
    return result

  def NoEmbedFontListRemoveIndex(self, Index):
    result = self.dpl.DPLNoEmbedFontListRemoveIndex(self.instanceID, Index)
    return result

  def NoEmbedFontListRemoveName(self, FontName):
    result = self.dpl.DPLNoEmbedFontListRemoveName(self.instanceID, FontName)
    return result

  def NormalizePage(self, NormalizeOptions):
    result = self.dpl.DPLNormalizePage(self.instanceID, NormalizeOptions)
    return result

  def OpenOutline(self, OutlineID):
    result = self.dpl.DPLOpenOutline(self.instanceID, OutlineID)
    return result

  def OptionalContentGroupCount(self):
    result = self.dpl.DPLOptionalContentGroupCount(self.instanceID)
    return result

  def OutlineCount(self):
    result = self.dpl.DPLOutlineCount(self.instanceID)
    return result

  def OutlineTitle(self, OutlineID):
    result = self.dpl.DPLOutlineTitle(self.instanceID, OutlineID)
    return result

  def PDFiumPrintDocument(self, PrinterName, StartPage, EndPage, Options):
    result = self.dpl.DPLPDFiumPrintDocument(self.instanceID, PrinterName, StartPage, EndPage, Options)
    return result

  def PageCount(self):
    result = self.dpl.DPLPageCount(self.instanceID)
    return result

  def PageHasFontResources(self, PageNumber):
    result = self.dpl.DPLPageHasFontResources(self.instanceID, PageNumber)
    return result

  def PageHeight(self):
    result = self.dpl.DPLPageHeight(self.instanceID)
    return result

  def PageJavaScriptAction(self, ActionType, JavaScript):
    result = self.dpl.DPLPageJavaScriptAction(self.instanceID, ActionType, JavaScript)
    return result

  def PageRotation(self):
    result = self.dpl.DPLPageRotation(self.instanceID)
    return result

  def PageWidth(self):
    result = self.dpl.DPLPageWidth(self.instanceID)
    return result

  def PrintDocument(self, PrinterName, StartPage, EndPage, Options):
    result = self.dpl.DPLPrintDocument(self.instanceID, PrinterName, StartPage, EndPage, Options)
    return result

  def PrintDocumentToFile(self, PrinterName, StartPage, EndPage, Options, FileName):
    result = self.dpl.DPLPrintDocumentToFile(self.instanceID, PrinterName, StartPage, EndPage, Options, FileName)
    return result

  def PrintMode(self, Mode):
    result = self.dpl.DPLPrintMode(self.instanceID, Mode)
    return result

  def PrintOptions(self, PageScaling, AutoRotateCenter, Title):
    result = self.dpl.DPLPrintOptions(self.instanceID, PageScaling, AutoRotateCenter, Title)
    return result

  def PrintPages(self, PrinterName, PageRanges, Options):
    result = self.dpl.DPLPrintPages(self.instanceID, PrinterName, PageRanges, Options)
    return result

  def PrintPagesToFile(self, PrinterName, PageRanges, Options, FileName):
    result = self.dpl.DPLPrintPagesToFile(self.instanceID, PrinterName, PageRanges, Options, FileName)
    return result

  def ReduceSize(self, Options):
    result = self.dpl.DPLReduceSize(self.instanceID, Options)
    return result

  def ReleaseBuffer(self, Buffer):
    BufferBuffer, BufferUsed = self.StringParm(Buffer)
    result = self.dpl.DPLReleaseBuffer(self.instanceID, BufferBuffer)
    if BufferUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, BufferBuffer)
    return result

  def ReleaseImage(self, ImageID):
    result = self.dpl.DPLReleaseImage(self.instanceID, ImageID)
    return result

  def ReleaseImageList(self, ImageListID):
    result = self.dpl.DPLReleaseImageList(self.instanceID, ImageListID)
    return result

  def ReleaseLibrary(self):
    result = self.dpl.DPLReleaseLibrary(self.instanceID)
    return result

  def ReleaseSignProcess(self, SignProcessID):
    result = self.dpl.DPLReleaseSignProcess(self.instanceID, SignProcessID)
    return result

  def ReleaseStringList(self, StringListID):
    result = self.dpl.DPLReleaseStringList(self.instanceID, StringListID)
    return result

  def ReleaseTextBlocks(self, TextBlockListID):
    result = self.dpl.DPLReleaseTextBlocks(self.instanceID, TextBlockListID)
    return result

  def RemoveAppearanceStream(self, Index):
    result = self.dpl.DPLRemoveAppearanceStream(self.instanceID, Index)
    return result

  def RemoveCustomInformation(self, Key):
    result = self.dpl.DPLRemoveCustomInformation(self.instanceID, Key)
    return result

  def RemoveDocument(self, DocumentID):
    result = self.dpl.DPLRemoveDocument(self.instanceID, DocumentID)
    return result

  def RemoveEmbeddedFile(self, Index):
    result = self.dpl.DPLRemoveEmbeddedFile(self.instanceID, Index)
    return result

  def RemoveFormFieldBackgroundColor(self, Index):
    result = self.dpl.DPLRemoveFormFieldBackgroundColor(self.instanceID, Index)
    return result

  def RemoveFormFieldBorderColor(self, Index):
    result = self.dpl.DPLRemoveFormFieldBorderColor(self.instanceID, Index)
    return result

  def RemoveFormFieldChoiceSub(self, Index, SubName):
    result = self.dpl.DPLRemoveFormFieldChoiceSub(self.instanceID, Index, SubName)
    return result

  def RemoveGlobalJavaScript(self, PackageName):
    result = self.dpl.DPLRemoveGlobalJavaScript(self.instanceID, PackageName)
    return result

  def RemoveOpenAction(self):
    result = self.dpl.DPLRemoveOpenAction(self.instanceID)
    return result

  def RemoveOutline(self, OutlineID):
    result = self.dpl.DPLRemoveOutline(self.instanceID, OutlineID)
    return result

  def RemovePageBox(self, BoxType):
    result = self.dpl.DPLRemovePageBox(self.instanceID, BoxType)
    return result

  def RemoveSharedContentStreams(self):
    result = self.dpl.DPLRemoveSharedContentStreams(self.instanceID)
    return result

  def RemoveStyle(self, StyleName):
    result = self.dpl.DPLRemoveStyle(self.instanceID, StyleName)
    return result

  def RemoveUsageRights(self):
    result = self.dpl.DPLRemoveUsageRights(self.instanceID)
    return result

  def RemoveXFAEntries(self, Options):
    result = self.dpl.DPLRemoveXFAEntries(self.instanceID, Options)
    return result

  def RenderAsMultipageTIFFToFile(self, DPI, PageRanges, ImageOptions, OutputOptions, FileName):
    result = self.dpl.DPLRenderAsMultipageTIFFToFile(self.instanceID, DPI, PageRanges, ImageOptions, OutputOptions, FileName)
    return result

  def RenderDocumentToFile(self, DPI, StartPage, EndPage, Options, FileName):
    result = self.dpl.DPLRenderDocumentToFile(self.instanceID, DPI, StartPage, EndPage, Options, FileName)
    return result

  def RenderPageToDC(self, DPI, Page, DC):
    result = self.dpl.DPLRenderPageToDC(self.instanceID, DPI, Page, DC)
    return result

  def RenderPageToFile(self, DPI, Page, Options, FileName):
    result = self.dpl.DPLRenderPageToFile(self.instanceID, DPI, Page, Options, FileName)
    return result

  def RenderPageToString(self, DPI, Page, Options):
    resultPtr = self.dpl.DPLRenderPageToString(self.instanceID, DPI, Page, Options)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def ReplaceFonts(self, Options):
    result = self.dpl.DPLReplaceFonts(self.instanceID, Options)
    return result

  def ReplaceImage(self, OriginalImageID, NewImageID):
    result = self.dpl.DPLReplaceImage(self.instanceID, OriginalImageID, NewImageID)
    return result

  def ReplaceTag(self, Tag, NewValue):
    result = self.dpl.DPLReplaceTag(self.instanceID, Tag, NewValue)
    return result

  def RequestPrinterStatus(self, StatusCommand):
    result = self.dpl.DPLRequestPrinterStatus(self.instanceID, StatusCommand)
    return result

  def RetrieveCustomDataToFile(self, Key, FileName, Location):
    result = self.dpl.DPLRetrieveCustomDataToFile(self.instanceID, Key, FileName, Location)
    return result

  def RetrieveCustomDataToString(self, Key, Location):
    resultPtr = self.dpl.DPLRetrieveCustomDataToString(self.instanceID, Key, Location)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def ReverseImage(self, Reset):
    result = self.dpl.DPLReverseImage(self.instanceID, Reset)
    return result

  def RotatePage(self, PageRotation):
    result = self.dpl.DPLRotatePage(self.instanceID, PageRotation)
    return result

  def SaveFontToFile(self, FileName):
    result = self.dpl.DPLSaveFontToFile(self.instanceID, FileName)
    return result

  def SaveImageListItemDataToFile(self, ImageListID, ImageIndex, Options, ImageFileName):
    result = self.dpl.DPLSaveImageListItemDataToFile(self.instanceID, ImageListID, ImageIndex, Options, ImageFileName)
    return result

  def SaveImageToFile(self, FileName):
    result = self.dpl.DPLSaveImageToFile(self.instanceID, FileName)
    return result

  def SaveImageToString(self):
    resultPtr = self.dpl.DPLSaveImageToString(self.instanceID)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def SaveState(self):
    result = self.dpl.DPLSaveState(self.instanceID)
    return result

  def SaveStyle(self, StyleName):
    result = self.dpl.DPLSaveStyle(self.instanceID, StyleName)
    return result

  def SaveToFile(self, FileName):
    result = self.dpl.DPLSaveToFile(self.instanceID, FileName)
    return result

  def SaveToString(self):
    resultPtr = self.dpl.DPLSaveToString(self.instanceID)
    resultLen = self.dpl.DPLAnsiStringResultLength(self.instanceID)
    result = bytearray(C.string_at(resultPtr, resultLen))
    return result

  def SecurityInfo(self, SecurityItem):
    result = self.dpl.DPLSecurityInfo(self.instanceID, SecurityItem)
    return result

  def SelectContentStream(self, NewIndex):
    result = self.dpl.DPLSelectContentStream(self.instanceID, NewIndex)
    return result

  def SelectDocument(self, DocumentID):
    result = self.dpl.DPLSelectDocument(self.instanceID, DocumentID)
    return result

  def SelectFont(self, FontID):
    result = self.dpl.DPLSelectFont(self.instanceID, FontID)
    return result

  def SelectImage(self, ImageID):
    result = self.dpl.DPLSelectImage(self.instanceID, ImageID)
    return result

  def SelectPage(self, PageNumber):
    result = self.dpl.DPLSelectPage(self.instanceID, PageNumber)
    return result

  def SelectRenderer(self, RendererID):
    result = self.dpl.DPLSelectRenderer(self.instanceID, RendererID)
    return result

  def SelectedDocument(self):
    result = self.dpl.DPLSelectedDocument(self.instanceID)
    return result

  def SelectedFont(self):
    result = self.dpl.DPLSelectedFont(self.instanceID)
    return result

  def SelectedImage(self):
    result = self.dpl.DPLSelectedImage(self.instanceID)
    return result

  def SelectedPage(self):
    result = self.dpl.DPLSelectedPage(self.instanceID)
    return result

  def SelectedRenderer(self):
    result = self.dpl.DPLSelectedRenderer(self.instanceID)
    return result

  def SetActionURL(self, ActionID, NewURL):
    result = self.dpl.DPLSetActionURL(self.instanceID, ActionID, NewURL)
    return result

  def SetAnnotBorderColor(self, Index, Red, Green, Blue):
    result = self.dpl.DPLSetAnnotBorderColor(self.instanceID, Index, Red, Green, Blue)
    return result

  def SetAnnotBorderStyle(self, Index, Width, Style, DashOn, DashOff):
    result = self.dpl.DPLSetAnnotBorderStyle(self.instanceID, Index, Width, Style, DashOn, DashOff)
    return result

  def SetAnnotContents(self, Index, NewContents):
    result = self.dpl.DPLSetAnnotContents(self.instanceID, Index, NewContents)
    return result

  def SetAnnotDblProperty(self, Index, Tag, NewValue):
    result = self.dpl.DPLSetAnnotDblProperty(self.instanceID, Index, Tag, NewValue)
    return result

  def SetAnnotIntProperty(self, Index, Tag, NewValue):
    result = self.dpl.DPLSetAnnotIntProperty(self.instanceID, Index, Tag, NewValue)
    return result

  def SetAnnotOptional(self, Index, OptionalContentGroupID):
    result = self.dpl.DPLSetAnnotOptional(self.instanceID, Index, OptionalContentGroupID)
    return result

  def SetAnnotQuadPoints(self, Index, QuadNumber, X1, Y1, X2, Y2, X3, Y3, X4, Y4):
    result = self.dpl.DPLSetAnnotQuadPoints(self.instanceID, Index, QuadNumber, X1, Y1, X2, Y2, X3, Y3, X4, Y4)
    return result

  def SetAnnotRect(self, Index, Left, Top, Width, Height):
    result = self.dpl.DPLSetAnnotRect(self.instanceID, Index, Left, Top, Width, Height)
    return result

  def SetAnnotStrProperty(self, Index, Tag, NewValue):
    result = self.dpl.DPLSetAnnotStrProperty(self.instanceID, Index, Tag, NewValue)
    return result

  def SetAnsiMode(self, NewAnsiMode):
    result = self.dpl.DPLSetAnsiMode(self.instanceID, NewAnsiMode)
    return result

  def SetAppendInputFromString(self, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetAppendInputFromString(self.instanceID, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetBaseURL(self, NewBaseURL):
    result = self.dpl.DPLSetBaseURL(self.instanceID, NewBaseURL)
    return result

  def SetBlendMode(self, BlendMode):
    result = self.dpl.DPLSetBlendMode(self.instanceID, BlendMode)
    return result

  def SetBreakString(self, NewBreakString):
    result = self.dpl.DPLSetBreakString(self.instanceID, NewBreakString)
    return result

  def SetCSDictEPSG(self, CSDictID, NewEPSG):
    result = self.dpl.DPLSetCSDictEPSG(self.instanceID, CSDictID, NewEPSG)
    return result

  def SetCSDictType(self, CSDictID, NewDictType):
    result = self.dpl.DPLSetCSDictType(self.instanceID, CSDictID, NewDictType)
    return result

  def SetCSDictWKT(self, CSDictID, NewWKT):
    result = self.dpl.DPLSetCSDictWKT(self.instanceID, CSDictID, NewWKT)
    return result

  def SetCairoFileName(self, FileName):
    result = self.dpl.DPLSetCairoFileName(self.instanceID, FileName)
    return result

  def SetCapturedPageOptional(self, CaptureID, OptionalContentGroupID):
    result = self.dpl.DPLSetCapturedPageOptional(self.instanceID, CaptureID, OptionalContentGroupID)
    return result

  def SetCapturedPageTransparencyGroup(self, CaptureID, CS, Isolate, Knockout):
    result = self.dpl.DPLSetCapturedPageTransparencyGroup(self.instanceID, CaptureID, CS, Isolate, Knockout)
    return result

  def SetCatalogInformation(self, Key, NewValue):
    result = self.dpl.DPLSetCatalogInformation(self.instanceID, Key, NewValue)
    return result

  def SetCharWidth(self, CharCode, NewWidth):
    result = self.dpl.DPLSetCharWidth(self.instanceID, CharCode, NewWidth)
    return result

  def SetClippingPath(self):
    result = self.dpl.DPLSetClippingPath(self.instanceID)
    return result

  def SetClippingPathEvenOdd(self):
    result = self.dpl.DPLSetClippingPathEvenOdd(self.instanceID)
    return result

  def SetCompatibility(self, CompatibilityItem, CompatibilityMode):
    result = self.dpl.DPLSetCompatibility(self.instanceID, CompatibilityItem, CompatibilityMode)
    return result

  def SetContentStreamFromString(self, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetContentStreamFromString(self.instanceID, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetContentStreamOptional(self, OptionalContentGroupID):
    result = self.dpl.DPLSetContentStreamOptional(self.instanceID, OptionalContentGroupID)
    return result

  def SetCropBox(self, Left, Top, Width, Height):
    result = self.dpl.DPLSetCropBox(self.instanceID, Left, Top, Width, Height)
    return result

  def SetCustomInformation(self, Key, NewValue):
    result = self.dpl.DPLSetCustomInformation(self.instanceID, Key, NewValue)
    return result

  def SetCustomLineDash(self, DashPattern, DashPhase):
    result = self.dpl.DPLSetCustomLineDash(self.instanceID, DashPattern, DashPhase)
    return result

  def SetDPLRFileName(self, FileName):
    result = self.dpl.DPLSetDPLRFileName(self.instanceID, FileName)
    return result

  def SetDecodeMode(self, NewDecodeMode):
    result = self.dpl.DPLSetDecodeMode(self.instanceID, NewDecodeMode)
    return result

  def SetDestProperties(self, DestID, Zoom, DestType, Left, Top, Right, Bottom):
    result = self.dpl.DPLSetDestProperties(self.instanceID, DestID, Zoom, DestType, Left, Top, Right, Bottom)
    return result

  def SetDestValue(self, DestID, ValueKey, NewValue):
    result = self.dpl.DPLSetDestValue(self.instanceID, DestID, ValueKey, NewValue)
    return result

  def SetDocumentMetadata(self, XMP):
    result = self.dpl.DPLSetDocumentMetadata(self.instanceID, XMP)
    return result

  def SetEmbeddedFileStrProperty(self, Index, Tag, NewValue):
    result = self.dpl.DPLSetEmbeddedFileStrProperty(self.instanceID, Index, Tag, NewValue)
    return result

  def SetFillColor(self, Red, Green, Blue):
    result = self.dpl.DPLSetFillColor(self.instanceID, Red, Green, Blue)
    return result

  def SetFillColorCMYK(self, C, M, Y, K):
    result = self.dpl.DPLSetFillColorCMYK(self.instanceID, C, M, Y, K)
    return result

  def SetFillColorSep(self, ColorName, Tint):
    result = self.dpl.DPLSetFillColorSep(self.instanceID, ColorName, Tint)
    return result

  def SetFillShader(self, ShaderName):
    result = self.dpl.DPLSetFillShader(self.instanceID, ShaderName)
    return result

  def SetFillTilingPattern(self, PatternName):
    result = self.dpl.DPLSetFillTilingPattern(self.instanceID, PatternName)
    return result

  def SetFindImagesMode(self, NewFindImagesMode):
    result = self.dpl.DPLSetFindImagesMode(self.instanceID, NewFindImagesMode)
    return result

  def SetFontEncoding(self, Encoding):
    result = self.dpl.DPLSetFontEncoding(self.instanceID, Encoding)
    return result

  def SetFontFlags(self, Fixed, Serif, Symbolic, Script, Italic, AllCap, SmallCap, ForceBold):
    result = self.dpl.DPLSetFontFlags(self.instanceID, Fixed, Serif, Symbolic, Script, Italic, AllCap, SmallCap, ForceBold)
    return result

  def SetFormFieldAlignment(self, Index, Alignment):
    result = self.dpl.DPLSetFormFieldAlignment(self.instanceID, Index, Alignment)
    return result

  def SetFormFieldAnnotFlags(self, Index, NewFlags):
    result = self.dpl.DPLSetFormFieldAnnotFlags(self.instanceID, Index, NewFlags)
    return result

  def SetFormFieldAppearanceFromString(self, Index, Source, FontID, FontReference):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetFormFieldAppearanceFromString(self.instanceID, Index, SourceBuffer, FontID, FontReference)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetFormFieldBackgroundColor(self, Index, Red, Green, Blue):
    result = self.dpl.DPLSetFormFieldBackgroundColor(self.instanceID, Index, Red, Green, Blue)
    return result

  def SetFormFieldBackgroundColorCMYK(self, Index, C, M, Y, K):
    result = self.dpl.DPLSetFormFieldBackgroundColorCMYK(self.instanceID, Index, C, M, Y, K)
    return result

  def SetFormFieldBackgroundColorGray(self, Index, Gray):
    result = self.dpl.DPLSetFormFieldBackgroundColorGray(self.instanceID, Index, Gray)
    return result

  def SetFormFieldBackgroundColorSep(self, Index, ColorName, Tint):
    result = self.dpl.DPLSetFormFieldBackgroundColorSep(self.instanceID, Index, ColorName, Tint)
    return result

  def SetFormFieldBorderColor(self, Index, Red, Green, Blue):
    result = self.dpl.DPLSetFormFieldBorderColor(self.instanceID, Index, Red, Green, Blue)
    return result

  def SetFormFieldBorderColorCMYK(self, Index, C, M, Y, K):
    result = self.dpl.DPLSetFormFieldBorderColorCMYK(self.instanceID, Index, C, M, Y, K)
    return result

  def SetFormFieldBorderColorGray(self, Index, Gray):
    result = self.dpl.DPLSetFormFieldBorderColorGray(self.instanceID, Index, Gray)
    return result

  def SetFormFieldBorderColorSep(self, Index, ColorName, Tint):
    result = self.dpl.DPLSetFormFieldBorderColorSep(self.instanceID, Index, ColorName, Tint)
    return result

  def SetFormFieldBorderStyle(self, Index, Width, Style, DashOn, DashOff):
    result = self.dpl.DPLSetFormFieldBorderStyle(self.instanceID, Index, Width, Style, DashOn, DashOff)
    return result

  def SetFormFieldBounds(self, Index, Left, Top, Width, Height):
    result = self.dpl.DPLSetFormFieldBounds(self.instanceID, Index, Left, Top, Width, Height)
    return result

  def SetFormFieldCalcOrder(self, Index, Order):
    result = self.dpl.DPLSetFormFieldCalcOrder(self.instanceID, Index, Order)
    return result

  def SetFormFieldCaption(self, Index, NewCaption):
    result = self.dpl.DPLSetFormFieldCaption(self.instanceID, Index, NewCaption)
    return result

  def SetFormFieldCheckStyle(self, Index, CheckStyle, Position):
    result = self.dpl.DPLSetFormFieldCheckStyle(self.instanceID, Index, CheckStyle, Position)
    return result

  def SetFormFieldCheckboxColor(self, Index, SetType, Red, Green, Blue):
    result = self.dpl.DPLSetFormFieldCheckboxColor(self.instanceID, Index, SetType, Red, Green, Blue)
    return result

  def SetFormFieldChildTitle(self, Index, NewTitle):
    result = self.dpl.DPLSetFormFieldChildTitle(self.instanceID, Index, NewTitle)
    return result

  def SetFormFieldChoiceSub(self, Index, SubIndex, SubName, DisplayName):
    result = self.dpl.DPLSetFormFieldChoiceSub(self.instanceID, Index, SubIndex, SubName, DisplayName)
    return result

  def SetFormFieldChoiceType(self, Index, ChoiceType):
    result = self.dpl.DPLSetFormFieldChoiceType(self.instanceID, Index, ChoiceType)
    return result

  def SetFormFieldColor(self, Index, Red, Green, Blue):
    result = self.dpl.DPLSetFormFieldColor(self.instanceID, Index, Red, Green, Blue)
    return result

  def SetFormFieldColorCMYK(self, Index, C, M, Y, K):
    result = self.dpl.DPLSetFormFieldColorCMYK(self.instanceID, Index, C, M, Y, K)
    return result

  def SetFormFieldColorSep(self, Index, ColorName, Tint):
    result = self.dpl.DPLSetFormFieldColorSep(self.instanceID, Index, ColorName, Tint)
    return result

  def SetFormFieldComb(self, Index, Comb):
    result = self.dpl.DPLSetFormFieldComb(self.instanceID, Index, Comb)
    return result

  def SetFormFieldCustomDict(self, Index, Key, NewValue, StorageType, Options):
    result = self.dpl.DPLSetFormFieldCustomDict(self.instanceID, Index, Key, NewValue, StorageType, Options)
    return result

  def SetFormFieldDefaultValue(self, Index, NewDefaultValue):
    result = self.dpl.DPLSetFormFieldDefaultValue(self.instanceID, Index, NewDefaultValue)
    return result

  def SetFormFieldDefaultValueEx(self, Index, NewDefaultValue, Options):
    result = self.dpl.DPLSetFormFieldDefaultValueEx(self.instanceID, Index, NewDefaultValue, Options)
    return result

  def SetFormFieldDescription(self, Index, NewDescription):
    result = self.dpl.DPLSetFormFieldDescription(self.instanceID, Index, NewDescription)
    return result

  def SetFormFieldFlags(self, Index, NewFlags):
    result = self.dpl.DPLSetFormFieldFlags(self.instanceID, Index, NewFlags)
    return result

  def SetFormFieldFont(self, Index, FontIndex):
    result = self.dpl.DPLSetFormFieldFont(self.instanceID, Index, FontIndex)
    return result

  def SetFormFieldFormatMode(self, NewFormatMode):
    result = self.dpl.DPLSetFormFieldFormatMode(self.instanceID, NewFormatMode)
    return result

  def SetFormFieldHighlightMode(self, Index, NewMode):
    result = self.dpl.DPLSetFormFieldHighlightMode(self.instanceID, Index, NewMode)
    return result

  def SetFormFieldIcon(self, Index, IconType, CaptureID):
    result = self.dpl.DPLSetFormFieldIcon(self.instanceID, Index, IconType, CaptureID)
    return result

  def SetFormFieldIconStyle(self, Index, Placement, Scale, ScaleType, HorizontalShift, VerticalShift):
    result = self.dpl.DPLSetFormFieldIconStyle(self.instanceID, Index, Placement, Scale, ScaleType, HorizontalShift, VerticalShift)
    return result

  def SetFormFieldLockAction(self, Index, LockAction, FieldList, Delimiter):
    result = self.dpl.DPLSetFormFieldLockAction(self.instanceID, Index, LockAction, FieldList, Delimiter)
    return result

  def SetFormFieldMaxLen(self, Index, NewMaxLen):
    result = self.dpl.DPLSetFormFieldMaxLen(self.instanceID, Index, NewMaxLen)
    return result

  def SetFormFieldMetadata(self, Index, XMP):
    result = self.dpl.DPLSetFormFieldMetadata(self.instanceID, Index, XMP)
    return result

  def SetFormFieldNoExport(self, Index, NoExport):
    result = self.dpl.DPLSetFormFieldNoExport(self.instanceID, Index, NoExport)
    return result

  def SetFormFieldOptional(self, Index, OptionalContentGroupID):
    result = self.dpl.DPLSetFormFieldOptional(self.instanceID, Index, OptionalContentGroupID)
    return result

  def SetFormFieldPage(self, Index, NewPage):
    result = self.dpl.DPLSetFormFieldPage(self.instanceID, Index, NewPage)
    return result

  def SetFormFieldPrintable(self, Index, Printable):
    result = self.dpl.DPLSetFormFieldPrintable(self.instanceID, Index, Printable)
    return result

  def SetFormFieldReadOnly(self, Index, ReadOnly):
    result = self.dpl.DPLSetFormFieldReadOnly(self.instanceID, Index, ReadOnly)
    return result

  def SetFormFieldRequired(self, Index, Required):
    result = self.dpl.DPLSetFormFieldRequired(self.instanceID, Index, Required)
    return result

  def SetFormFieldResetAction(self, Index, ActionType):
    result = self.dpl.DPLSetFormFieldResetAction(self.instanceID, Index, ActionType)
    return result

  def SetFormFieldRichTextString(self, Index, Key, NewValue):
    result = self.dpl.DPLSetFormFieldRichTextString(self.instanceID, Index, Key, NewValue)
    return result

  def SetFormFieldRotation(self, Index, Angle):
    result = self.dpl.DPLSetFormFieldRotation(self.instanceID, Index, Angle)
    return result

  def SetFormFieldSignatureImage(self, Index, ImageID, Options):
    result = self.dpl.DPLSetFormFieldSignatureImage(self.instanceID, Index, ImageID, Options)
    return result

  def SetFormFieldStandardFont(self, Index, StandardFontID):
    result = self.dpl.DPLSetFormFieldStandardFont(self.instanceID, Index, StandardFontID)
    return result

  def SetFormFieldSubmitAction(self, Index, ActionType, Link):
    result = self.dpl.DPLSetFormFieldSubmitAction(self.instanceID, Index, ActionType, Link)
    return result

  def SetFormFieldSubmitActionEx(self, Index, ActionType, Link, Flags):
    result = self.dpl.DPLSetFormFieldSubmitActionEx(self.instanceID, Index, ActionType, Link, Flags)
    return result

  def SetFormFieldTabOrder(self, Index, Order):
    result = self.dpl.DPLSetFormFieldTabOrder(self.instanceID, Index, Order)
    return result

  def SetFormFieldTextFlags(self, Index, Multiline, Password, FileSelect, DoNotSpellCheck, DoNotScroll):
    result = self.dpl.DPLSetFormFieldTextFlags(self.instanceID, Index, Multiline, Password, FileSelect, DoNotSpellCheck, DoNotScroll)
    return result

  def SetFormFieldTextSize(self, Index, NewTextSize):
    result = self.dpl.DPLSetFormFieldTextSize(self.instanceID, Index, NewTextSize)
    return result

  def SetFormFieldTitle(self, Index, NewTitle):
    result = self.dpl.DPLSetFormFieldTitle(self.instanceID, Index, NewTitle)
    return result

  def SetFormFieldValue(self, Index, NewValue):
    result = self.dpl.DPLSetFormFieldValue(self.instanceID, Index, NewValue)
    return result

  def SetFormFieldValueByTitle(self, Title, NewValue):
    result = self.dpl.DPLSetFormFieldValueByTitle(self.instanceID, Title, NewValue)
    return result

  def SetFormFieldValueEx(self, Index, NewValue, Options):
    result = self.dpl.DPLSetFormFieldValueEx(self.instanceID, Index, NewValue, Options)
    return result

  def SetFormFieldVisible(self, Index, Visible):
    result = self.dpl.DPLSetFormFieldVisible(self.instanceID, Index, Visible)
    return result

  def SetGDIPlusFileName(self, DLLFileName):
    result = self.dpl.DPLSetGDIPlusFileName(self.instanceID, DLLFileName)
    return result

  def SetGDIPlusOptions(self, OptionID, NewValue):
    result = self.dpl.DPLSetGDIPlusOptions(self.instanceID, OptionID, NewValue)
    return result

  def SetHTMLBoldFont(self, FontSet, FontID):
    result = self.dpl.DPLSetHTMLBoldFont(self.instanceID, FontSet, FontID)
    return result

  def SetHTMLBoldItalicFont(self, FontSet, FontID):
    result = self.dpl.DPLSetHTMLBoldItalicFont(self.instanceID, FontSet, FontID)
    return result

  def SetHTMLItalicFont(self, FontSet, FontID):
    result = self.dpl.DPLSetHTMLItalicFont(self.instanceID, FontSet, FontID)
    return result

  def SetHTMLNormalFont(self, FontSet, FontID):
    result = self.dpl.DPLSetHTMLNormalFont(self.instanceID, FontSet, FontID)
    return result

  def SetHeaderCommentsFromString(self, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetHeaderCommentsFromString(self.instanceID, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetImageAsMask(self, MaskType):
    result = self.dpl.DPLSetImageAsMask(self.instanceID, MaskType)
    return result

  def SetImageMask(self, FromRed, FromGreen, FromBlue, ToRed, ToGreen, ToBlue):
    result = self.dpl.DPLSetImageMask(self.instanceID, FromRed, FromGreen, FromBlue, ToRed, ToGreen, ToBlue)
    return result

  def SetImageMaskCMYK(self, FromC, FromM, FromY, FromK, ToC, ToM, ToY, ToK):
    result = self.dpl.DPLSetImageMaskCMYK(self.instanceID, FromC, FromM, FromY, FromK, ToC, ToM, ToY, ToK)
    return result

  def SetImageMaskFromImage(self, ImageID):
    result = self.dpl.DPLSetImageMaskFromImage(self.instanceID, ImageID)
    return result

  def SetImageOptional(self, OptionalContentGroupID):
    result = self.dpl.DPLSetImageOptional(self.instanceID, OptionalContentGroupID)
    return result

  def SetImageResolution(self, Horizontal, Vertical, Units):
    result = self.dpl.DPLSetImageResolution(self.instanceID, Horizontal, Vertical, Units)
    return result

  def SetInformation(self, Key, NewValue):
    result = self.dpl.DPLSetInformation(self.instanceID, Key, NewValue)
    return result

  def SetJPEGQuality(self, Quality):
    result = self.dpl.DPLSetJPEGQuality(self.instanceID, Quality)
    return result

  def SetJavaScriptMode(self, JSMode):
    result = self.dpl.DPLSetJavaScriptMode(self.instanceID, JSMode)
    return result

  def SetKerning(self, CharPair, Adjustment):
    result = self.dpl.DPLSetKerning(self.instanceID, CharPair, Adjustment)
    return result

  def SetLineCap(self, LineCap):
    result = self.dpl.DPLSetLineCap(self.instanceID, LineCap)
    return result

  def SetLineColor(self, Red, Green, Blue):
    result = self.dpl.DPLSetLineColor(self.instanceID, Red, Green, Blue)
    return result

  def SetLineColorCMYK(self, C, M, Y, K):
    result = self.dpl.DPLSetLineColorCMYK(self.instanceID, C, M, Y, K)
    return result

  def SetLineColorSep(self, ColorName, Tint):
    result = self.dpl.DPLSetLineColorSep(self.instanceID, ColorName, Tint)
    return result

  def SetLineDash(self, DashOn, DashOff):
    result = self.dpl.DPLSetLineDash(self.instanceID, DashOn, DashOff)
    return result

  def SetLineDashEx(self, DashValues):
    result = self.dpl.DPLSetLineDashEx(self.instanceID, DashValues)
    return result

  def SetLineJoin(self, LineJoin):
    result = self.dpl.DPLSetLineJoin(self.instanceID, LineJoin)
    return result

  def SetLineShader(self, ShaderName):
    result = self.dpl.DPLSetLineShader(self.instanceID, ShaderName)
    return result

  def SetLineWidth(self, LineWidth):
    result = self.dpl.DPLSetLineWidth(self.instanceID, LineWidth)
    return result

  def SetMarkupAnnotStyle(self, Index, Red, Green, Blue, Transparency):
    result = self.dpl.DPLSetMarkupAnnotStyle(self.instanceID, Index, Red, Green, Blue, Transparency)
    return result

  def SetMeasureDictBoundsCount(self, MeasureDictID, NewCount):
    result = self.dpl.DPLSetMeasureDictBoundsCount(self.instanceID, MeasureDictID, NewCount)
    return result

  def SetMeasureDictBoundsItem(self, MeasureDictID, ItemIndex, NewValue):
    result = self.dpl.DPLSetMeasureDictBoundsItem(self.instanceID, MeasureDictID, ItemIndex, NewValue)
    return result

  def SetMeasureDictCoordinateSystem(self, MeasureDictID, CoordinateSystemID):
    result = self.dpl.DPLSetMeasureDictCoordinateSystem(self.instanceID, MeasureDictID, CoordinateSystemID)
    return result

  def SetMeasureDictGPTSCount(self, MeasureDictID, NewCount):
    result = self.dpl.DPLSetMeasureDictGPTSCount(self.instanceID, MeasureDictID, NewCount)
    return result

  def SetMeasureDictGPTSItem(self, MeasureDictID, ItemIndex, NewValue):
    result = self.dpl.DPLSetMeasureDictGPTSItem(self.instanceID, MeasureDictID, ItemIndex, NewValue)
    return result

  def SetMeasureDictLPTSCount(self, MeasureDictID, NewCount):
    result = self.dpl.DPLSetMeasureDictLPTSCount(self.instanceID, MeasureDictID, NewCount)
    return result

  def SetMeasureDictLPTSItem(self, MeasureDictID, ItemIndex, NewValue):
    result = self.dpl.DPLSetMeasureDictLPTSItem(self.instanceID, MeasureDictID, ItemIndex, NewValue)
    return result

  def SetMeasureDictPDU(self, MeasureDictID, LinearUnit, AreaUnit, AngularUnit):
    result = self.dpl.DPLSetMeasureDictPDU(self.instanceID, MeasureDictID, LinearUnit, AreaUnit, AngularUnit)
    return result

  def SetMeasurementUnits(self, MeasurementUnits):
    result = self.dpl.DPLSetMeasurementUnits(self.instanceID, MeasurementUnits)
    return result

  def SetMetafileMode(self, Mode):
    result = self.dpl.DPLSetMetafileMode(self.instanceID, Mode)
    return result

  def SetNeedAppearances(self, NewValue):
    result = self.dpl.DPLSetNeedAppearances(self.instanceID, NewValue)
    return result

  def SetObjectAsStreamFromString(self, ObjectNumber, Source, Options):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetObjectAsStreamFromString(self.instanceID, ObjectNumber, SourceBuffer, Options)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetObjectFromString(self, ObjectNumber, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetObjectFromString(self.instanceID, ObjectNumber, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetOpenActionDestination(self, OpenPage, Zoom):
    result = self.dpl.DPLSetOpenActionDestination(self.instanceID, OpenPage, Zoom)
    return result

  def SetOpenActionDestinationFull(self, OpenPage, Zoom, DestType, Left, Top, Right, Bottom):
    result = self.dpl.DPLSetOpenActionDestinationFull(self.instanceID, OpenPage, Zoom, DestType, Left, Top, Right, Bottom)
    return result

  def SetOpenActionJavaScript(self, JavaScript):
    result = self.dpl.DPLSetOpenActionJavaScript(self.instanceID, JavaScript)
    return result

  def SetOpenActionMenu(self, MenuItem):
    result = self.dpl.DPLSetOpenActionMenu(self.instanceID, MenuItem)
    return result

  def SetOptionalContentConfigLocked(self, OptionalContentConfigID, OptionalContentGroupID, NewLocked):
    result = self.dpl.DPLSetOptionalContentConfigLocked(self.instanceID, OptionalContentConfigID, OptionalContentGroupID, NewLocked)
    return result

  def SetOptionalContentConfigState(self, OptionalContentConfigID, OptionalContentGroupID, NewState):
    result = self.dpl.DPLSetOptionalContentConfigState(self.instanceID, OptionalContentConfigID, OptionalContentGroupID, NewState)
    return result

  def SetOptionalContentGroupName(self, OptionalContentGroupID, NewGroupName):
    result = self.dpl.DPLSetOptionalContentGroupName(self.instanceID, OptionalContentGroupID, NewGroupName)
    return result

  def SetOptionalContentGroupPrintable(self, OptionalContentGroupID, Printable):
    result = self.dpl.DPLSetOptionalContentGroupPrintable(self.instanceID, OptionalContentGroupID, Printable)
    return result

  def SetOptionalContentGroupVisible(self, OptionalContentGroupID, Visible):
    result = self.dpl.DPLSetOptionalContentGroupVisible(self.instanceID, OptionalContentGroupID, Visible)
    return result

  def SetOrigin(self, Origin):
    result = self.dpl.DPLSetOrigin(self.instanceID, Origin)
    return result

  def SetOutlineColor(self, OutlineID, Red, Green, Blue):
    result = self.dpl.DPLSetOutlineColor(self.instanceID, OutlineID, Red, Green, Blue)
    return result

  def SetOutlineDestination(self, OutlineID, DestPage, DestPosition):
    result = self.dpl.DPLSetOutlineDestination(self.instanceID, OutlineID, DestPage, DestPosition)
    return result

  def SetOutlineDestinationFull(self, OutlineID, DestPage, Zoom, DestType, Left, Top, Right, Bottom):
    result = self.dpl.DPLSetOutlineDestinationFull(self.instanceID, OutlineID, DestPage, Zoom, DestType, Left, Top, Right, Bottom)
    return result

  def SetOutlineDestinationZoom(self, OutlineID, DestPage, DestPosition, Zoom):
    result = self.dpl.DPLSetOutlineDestinationZoom(self.instanceID, OutlineID, DestPage, DestPosition, Zoom)
    return result

  def SetOutlineJavaScript(self, OutlineID, JavaScript):
    result = self.dpl.DPLSetOutlineJavaScript(self.instanceID, OutlineID, JavaScript)
    return result

  def SetOutlineNamedDestination(self, OutlineID, DestName):
    result = self.dpl.DPLSetOutlineNamedDestination(self.instanceID, OutlineID, DestName)
    return result

  def SetOutlineOpenFile(self, OutlineID, FileName):
    result = self.dpl.DPLSetOutlineOpenFile(self.instanceID, OutlineID, FileName)
    return result

  def SetOutlineRemoteDestination(self, OutlineID, FileName, OpenPage, Zoom, DestType, PntLeft, PntTop, PntRight, PntBottom, NewWindow):
    result = self.dpl.DPLSetOutlineRemoteDestination(self.instanceID, OutlineID, FileName, OpenPage, Zoom, DestType, PntLeft, PntTop, PntRight, PntBottom, NewWindow)
    return result

  def SetOutlineStyle(self, OutlineID, SetItalic, SetBold):
    result = self.dpl.DPLSetOutlineStyle(self.instanceID, OutlineID, SetItalic, SetBold)
    return result

  def SetOutlineTitle(self, OutlineID, NewTitle):
    result = self.dpl.DPLSetOutlineTitle(self.instanceID, OutlineID, NewTitle)
    return result

  def SetOutlineWebLink(self, OutlineID, Link):
    result = self.dpl.DPLSetOutlineWebLink(self.instanceID, OutlineID, Link)
    return result

  def SetOverprint(self, StrokingOverprint, OtherOverprint, OverprintMode):
    result = self.dpl.DPLSetOverprint(self.instanceID, StrokingOverprint, OtherOverprint, OverprintMode)
    return result

  def SetPDFAMode(self, NewMode):
    result = self.dpl.DPLSetPDFAMode(self.instanceID, NewMode)
    return result

  def SetPDFiumFileName(self, FileName):
    result = self.dpl.DPLSetPDFiumFileName(self.instanceID, FileName)
    return result

  def SetPNGTransparencyColor(self, RedByte, GreenByte, BlueByte):
    result = self.dpl.DPLSetPNGTransparencyColor(self.instanceID, RedByte, GreenByte, BlueByte)
    return result

  def SetPageActionMenu(self, MenuItem):
    result = self.dpl.DPLSetPageActionMenu(self.instanceID, MenuItem)
    return result

  def SetPageBox(self, BoxType, Left, Top, Width, Height):
    result = self.dpl.DPLSetPageBox(self.instanceID, BoxType, Left, Top, Width, Height)
    return result

  def SetPageContentFromString(self, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetPageContentFromString(self.instanceID, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetPageDimensions(self, NewPageWidth, NewPageHeight):
    result = self.dpl.DPLSetPageDimensions(self.instanceID, NewPageWidth, NewPageHeight)
    return result

  def SetPageLayout(self, NewPageLayout):
    result = self.dpl.DPLSetPageLayout(self.instanceID, NewPageLayout)
    return result

  def SetPageMetadata(self, XMP):
    result = self.dpl.DPLSetPageMetadata(self.instanceID, XMP)
    return result

  def SetPageMode(self, NewPageMode):
    result = self.dpl.DPLSetPageMode(self.instanceID, NewPageMode)
    return result

  def SetPageSize(self, PaperName):
    result = self.dpl.DPLSetPageSize(self.instanceID, PaperName)
    return result

  def SetPageThumbnail(self):
    result = self.dpl.DPLSetPageThumbnail(self.instanceID)
    return result

  def SetPageTransparencyGroup(self, CS, Isolate, Knockout):
    result = self.dpl.DPLSetPageTransparencyGroup(self.instanceID, CS, Isolate, Knockout)
    return result

  def SetPageUserUnit(self, UserUnit):
    result = self.dpl.DPLSetPageUserUnit(self.instanceID, UserUnit)
    return result

  def SetPrecision(self, NewPrecision):
    result = self.dpl.DPLSetPrecision(self.instanceID, NewPrecision)
    return result

  def SetPrinterDevModeFromString(self, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetPrinterDevModeFromString(self.instanceID, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetRenderArea(self, Left, Top, Width, Height):
    result = self.dpl.DPLSetRenderArea(self.instanceID, Left, Top, Width, Height)
    return result

  def SetRenderCropType(self, NewCropType):
    result = self.dpl.DPLSetRenderCropType(self.instanceID, NewCropType)
    return result

  def SetRenderDCErasePage(self, NewErasePage):
    result = self.dpl.DPLSetRenderDCErasePage(self.instanceID, NewErasePage)
    return result

  def SetRenderDCOffset(self, NewOffsetX, NewOffsetY):
    result = self.dpl.DPLSetRenderDCOffset(self.instanceID, NewOffsetX, NewOffsetY)
    return result

  def SetRenderOptions(self, OptionID, NewValue):
    result = self.dpl.DPLSetRenderOptions(self.instanceID, OptionID, NewValue)
    return result

  def SetRenderScale(self, NewScale):
    result = self.dpl.DPLSetRenderScale(self.instanceID, NewScale)
    return result

  def SetScale(self, NewScale):
    result = self.dpl.DPLSetScale(self.instanceID, NewScale)
    return result

  def SetSignProcessAppearanceFromString(self, SignProcessID, LayerName, Source):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetSignProcessAppearanceFromString(self.instanceID, SignProcessID, LayerName, SourceBuffer)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetSignProcessCertFromStore(self, SignProcessID, CertHash, Options):
    result = self.dpl.DPLSetSignProcessCertFromStore(self.instanceID, SignProcessID, CertHash, Options)
    return result

  def SetSignProcessCustomDict(self, SignProcessID, Key, NewValue, StorageType):
    result = self.dpl.DPLSetSignProcessCustomDict(self.instanceID, SignProcessID, Key, NewValue, StorageType)
    return result

  def SetSignProcessCustomSubFilter(self, SignProcessID, SubFilterStr):
    result = self.dpl.DPLSetSignProcessCustomSubFilter(self.instanceID, SignProcessID, SubFilterStr)
    return result

  def SetSignProcessField(self, SignProcessID, SignatureFieldName):
    result = self.dpl.DPLSetSignProcessField(self.instanceID, SignProcessID, SignatureFieldName)
    return result

  def SetSignProcessFieldBounds(self, SignProcessID, Left, Top, Width, Height):
    result = self.dpl.DPLSetSignProcessFieldBounds(self.instanceID, SignProcessID, Left, Top, Width, Height)
    return result

  def SetSignProcessFieldImageFromFile(self, SignProcessID, ImageFileName, Options):
    result = self.dpl.DPLSetSignProcessFieldImageFromFile(self.instanceID, SignProcessID, ImageFileName, Options)
    return result

  def SetSignProcessFieldImageFromString(self, SignProcessID, Source, Options):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetSignProcessFieldImageFromString(self.instanceID, SignProcessID, SourceBuffer, Options)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetSignProcessFieldLocked(self, SignProcessID, LockFieldAfterSign):
    result = self.dpl.DPLSetSignProcessFieldLocked(self.instanceID, SignProcessID, LockFieldAfterSign)
    return result

  def SetSignProcessFieldMetadata(self, SignProcessID, XMP):
    result = self.dpl.DPLSetSignProcessFieldMetadata(self.instanceID, SignProcessID, XMP)
    return result

  def SetSignProcessFieldPage(self, SignProcessID, SignaturePage):
    result = self.dpl.DPLSetSignProcessFieldPage(self.instanceID, SignProcessID, SignaturePage)
    return result

  def SetSignProcessImageLayer(self, SignProcessID, LayerName):
    result = self.dpl.DPLSetSignProcessImageLayer(self.instanceID, SignProcessID, LayerName)
    return result

  def SetSignProcessInfo(self, SignProcessID, Reason, Location, ContactInfo):
    result = self.dpl.DPLSetSignProcessInfo(self.instanceID, SignProcessID, Reason, Location, ContactInfo)
    return result

  def SetSignProcessKeyset(self, SignProcessID, KeysetID):
    result = self.dpl.DPLSetSignProcessKeyset(self.instanceID, SignProcessID, KeysetID)
    return result

  def SetSignProcessOptions(self, SignProcessID, OptionID, OptionValue):
    result = self.dpl.DPLSetSignProcessOptions(self.instanceID, SignProcessID, OptionID, OptionValue)
    return result

  def SetSignProcessPFXFromFile(self, SignProcessID, PFXFileName, PFXPassword):
    result = self.dpl.DPLSetSignProcessPFXFromFile(self.instanceID, SignProcessID, PFXFileName, PFXPassword)
    return result

  def SetSignProcessPFXFromString(self, SignProcessID, Source, PFXPassword):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetSignProcessPFXFromString(self.instanceID, SignProcessID, SourceBuffer, PFXPassword)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetSignProcessPassthrough(self, SignProcessID, SignatureLength):
    result = self.dpl.DPLSetSignProcessPassthrough(self.instanceID, SignProcessID, SignatureLength)
    return result

  def SetSignProcessSubFilter(self, SignProcessID, SubFilter):
    result = self.dpl.DPLSetSignProcessSubFilter(self.instanceID, SignProcessID, SubFilter)
    return result

  def SetTabOrderMode(self, Mode):
    result = self.dpl.DPLSetTabOrderMode(self.instanceID, Mode)
    return result

  def SetTableBorderColor(self, TableID, BorderIndex, Red, Green, Blue):
    result = self.dpl.DPLSetTableBorderColor(self.instanceID, TableID, BorderIndex, Red, Green, Blue)
    return result

  def SetTableBorderColorCMYK(self, TableID, BorderIndex, C, M, Y, K):
    result = self.dpl.DPLSetTableBorderColorCMYK(self.instanceID, TableID, BorderIndex, C, M, Y, K)
    return result

  def SetTableBorderWidth(self, TableID, BorderIndex, NewWidth):
    result = self.dpl.DPLSetTableBorderWidth(self.instanceID, TableID, BorderIndex, NewWidth)
    return result

  def SetTableCellAlignment(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, NewCellAlignment):
    result = self.dpl.DPLSetTableCellAlignment(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, NewCellAlignment)
    return result

  def SetTableCellBackgroundColor(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, Red, Green, Blue):
    result = self.dpl.DPLSetTableCellBackgroundColor(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, Red, Green, Blue)
    return result

  def SetTableCellBackgroundColorCMYK(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, C, M, Y, K):
    result = self.dpl.DPLSetTableCellBackgroundColorCMYK(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, C, M, Y, K)
    return result

  def SetTableCellBorderColor(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, BorderIndex, Red, Green, Blue):
    result = self.dpl.DPLSetTableCellBorderColor(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, BorderIndex, Red, Green, Blue)
    return result

  def SetTableCellBorderColorCMYK(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, BorderIndex, C, M, Y, K):
    result = self.dpl.DPLSetTableCellBorderColorCMYK(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, BorderIndex, C, M, Y, K)
    return result

  def SetTableCellBorderWidth(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, BorderIndex, NewWidth):
    result = self.dpl.DPLSetTableCellBorderWidth(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, BorderIndex, NewWidth)
    return result

  def SetTableCellContent(self, TableID, RowNumber, ColumnNumber, HTMLText):
    result = self.dpl.DPLSetTableCellContent(self.instanceID, TableID, RowNumber, ColumnNumber, HTMLText)
    return result

  def SetTableCellPadding(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, BorderIndex, NewPadding):
    result = self.dpl.DPLSetTableCellPadding(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, BorderIndex, NewPadding)
    return result

  def SetTableCellTextColor(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, Red, Green, Blue):
    result = self.dpl.DPLSetTableCellTextColor(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, Red, Green, Blue)
    return result

  def SetTableCellTextColorCMYK(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, C, M, Y, K):
    result = self.dpl.DPLSetTableCellTextColorCMYK(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, C, M, Y, K)
    return result

  def SetTableCellTextSize(self, TableID, FirstRow, FirstColumn, LastRow, LastColumn, NewTextSize):
    result = self.dpl.DPLSetTableCellTextSize(self.instanceID, TableID, FirstRow, FirstColumn, LastRow, LastColumn, NewTextSize)
    return result

  def SetTableColumnWidth(self, TableID, FirstColumn, LastColumn, NewWidth):
    result = self.dpl.DPLSetTableColumnWidth(self.instanceID, TableID, FirstColumn, LastColumn, NewWidth)
    return result

  def SetTableRowHeight(self, TableID, FirstRow, LastRow, NewHeight):
    result = self.dpl.DPLSetTableRowHeight(self.instanceID, TableID, FirstRow, LastRow, NewHeight)
    return result

  def SetTableThinBorders(self, TableID, ThinBorders, Red, Green, Blue):
    result = self.dpl.DPLSetTableThinBorders(self.instanceID, TableID, ThinBorders, Red, Green, Blue)
    return result

  def SetTableThinBordersCMYK(self, TableID, ThinBorders, C, M, Y, K):
    result = self.dpl.DPLSetTableThinBordersCMYK(self.instanceID, TableID, ThinBorders, C, M, Y, K)
    return result

  def SetTempFile(self, FileName):
    result = self.dpl.DPLSetTempFile(self.instanceID, FileName)
    return result

  def SetTempPath(self, NewPath):
    result = self.dpl.DPLSetTempPath(self.instanceID, NewPath)
    return result

  def SetTextAlign(self, TextAlign):
    result = self.dpl.DPLSetTextAlign(self.instanceID, TextAlign)
    return result

  def SetTextCharSpacing(self, CharSpacing):
    result = self.dpl.DPLSetTextCharSpacing(self.instanceID, CharSpacing)
    return result

  def SetTextColor(self, Red, Green, Blue):
    result = self.dpl.DPLSetTextColor(self.instanceID, Red, Green, Blue)
    return result

  def SetTextColorCMYK(self, C, M, Y, K):
    result = self.dpl.DPLSetTextColorCMYK(self.instanceID, C, M, Y, K)
    return result

  def SetTextColorSep(self, ColorName, Tint):
    result = self.dpl.DPLSetTextColorSep(self.instanceID, ColorName, Tint)
    return result

  def SetTextExtractionArea(self, Left, Top, Width, Height):
    result = self.dpl.DPLSetTextExtractionArea(self.instanceID, Left, Top, Width, Height)
    return result

  def SetTextExtractionOptions(self, OptionID, NewValue):
    result = self.dpl.DPLSetTextExtractionOptions(self.instanceID, OptionID, NewValue)
    return result

  def SetTextExtractionScaling(self, Options, Horizontal, Vertical):
    result = self.dpl.DPLSetTextExtractionScaling(self.instanceID, Options, Horizontal, Vertical)
    return result

  def SetTextExtractionWordGap(self, NewWordGap):
    result = self.dpl.DPLSetTextExtractionWordGap(self.instanceID, NewWordGap)
    return result

  def SetTextHighlight(self, Highlight):
    result = self.dpl.DPLSetTextHighlight(self.instanceID, Highlight)
    return result

  def SetTextHighlightColor(self, Red, Green, Blue):
    result = self.dpl.DPLSetTextHighlightColor(self.instanceID, Red, Green, Blue)
    return result

  def SetTextHighlightColorCMYK(self, C, M, Y, K):
    result = self.dpl.DPLSetTextHighlightColorCMYK(self.instanceID, C, M, Y, K)
    return result

  def SetTextHighlightColorSep(self, ColorName, Tint):
    result = self.dpl.DPLSetTextHighlightColorSep(self.instanceID, ColorName, Tint)
    return result

  def SetTextMode(self, TextMode):
    result = self.dpl.DPLSetTextMode(self.instanceID, TextMode)
    return result

  def SetTextRise(self, Rise):
    result = self.dpl.DPLSetTextRise(self.instanceID, Rise)
    return result

  def SetTextScaling(self, ScalePercentage):
    result = self.dpl.DPLSetTextScaling(self.instanceID, ScalePercentage)
    return result

  def SetTextShader(self, ShaderName):
    result = self.dpl.DPLSetTextShader(self.instanceID, ShaderName)
    return result

  def SetTextSize(self, TextSize):
    result = self.dpl.DPLSetTextSize(self.instanceID, TextSize)
    return result

  def SetTextSpacing(self, Spacing):
    result = self.dpl.DPLSetTextSpacing(self.instanceID, Spacing)
    return result

  def SetTextUnderline(self, Underline):
    result = self.dpl.DPLSetTextUnderline(self.instanceID, Underline)
    return result

  def SetTextUnderlineColor(self, Red, Green, Blue):
    result = self.dpl.DPLSetTextUnderlineColor(self.instanceID, Red, Green, Blue)
    return result

  def SetTextUnderlineColorCMYK(self, C, M, Y, K):
    result = self.dpl.DPLSetTextUnderlineColorCMYK(self.instanceID, C, M, Y, K)
    return result

  def SetTextUnderlineColorSep(self, ColorName, Tint):
    result = self.dpl.DPLSetTextUnderlineColorSep(self.instanceID, ColorName, Tint)
    return result

  def SetTextUnderlineCustomDash(self, DashPattern, DashPhase):
    result = self.dpl.DPLSetTextUnderlineCustomDash(self.instanceID, DashPattern, DashPhase)
    return result

  def SetTextUnderlineDash(self, DashOn, DashOff):
    result = self.dpl.DPLSetTextUnderlineDash(self.instanceID, DashOn, DashOff)
    return result

  def SetTextUnderlineDistance(self, UnderlineDistance):
    result = self.dpl.DPLSetTextUnderlineDistance(self.instanceID, UnderlineDistance)
    return result

  def SetTextUnderlineWidth(self, UnderlineWidth):
    result = self.dpl.DPLSetTextUnderlineWidth(self.instanceID, UnderlineWidth)
    return result

  def SetTextWordSpacing(self, WordSpacing):
    result = self.dpl.DPLSetTextWordSpacing(self.instanceID, WordSpacing)
    return result

  def SetTransparency(self, Transparency):
    result = self.dpl.DPLSetTransparency(self.instanceID, Transparency)
    return result

  def SetUpdateMode(self, NewUpdateMode):
    result = self.dpl.DPLSetUpdateMode(self.instanceID, NewUpdateMode)
    return result

  def SetViewerPreferences(self, Option, NewValue):
    result = self.dpl.DPLSetViewerPreferences(self.instanceID, Option, NewValue)
    return result

  def SetXFAFormFieldAccess(self, XFAFieldName, NewAccess):
    result = self.dpl.DPLSetXFAFormFieldAccess(self.instanceID, XFAFieldName, NewAccess)
    return result

  def SetXFAFormFieldBorderColor(self, XFAFieldName, Red, Green, Blue):
    result = self.dpl.DPLSetXFAFormFieldBorderColor(self.instanceID, XFAFieldName, Red, Green, Blue)
    return result

  def SetXFAFormFieldBorderPresence(self, XFAFieldName, NewPresence):
    result = self.dpl.DPLSetXFAFormFieldBorderPresence(self.instanceID, XFAFieldName, NewPresence)
    return result

  def SetXFAFormFieldBorderWidth(self, XFAFieldName, BorderWidth):
    result = self.dpl.DPLSetXFAFormFieldBorderWidth(self.instanceID, XFAFieldName, BorderWidth)
    return result

  def SetXFAFormFieldValue(self, XFAFieldName, NewValue):
    result = self.dpl.DPLSetXFAFormFieldValue(self.instanceID, XFAFieldName, NewValue)
    return result

  def SetXFAFromString(self, Source, Options):
    SourceBuffer, SourceUsed = self.StringParm(Source)
    result = self.dpl.DPLSetXFAFromString(self.instanceID, SourceBuffer, Options)
    if SourceUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, SourceBuffer)
    return result

  def SetupCustomPrinter(self, CustomPrinterName, Setting, NewValue):
    result = self.dpl.DPLSetupCustomPrinter(self.instanceID, CustomPrinterName, Setting, NewValue)
    return result

  def SignFile(self, InputFileName, OpenPassword, SignatureFieldName, OutputFileName, PFXFileName, PFXPassword, Reason, Location, ContactInfo):
    result = self.dpl.DPLSignFile(self.instanceID, InputFileName, OpenPassword, SignatureFieldName, OutputFileName, PFXFileName, PFXPassword, Reason, Location, ContactInfo)
    return result

  def SplitPageText(self, Options):
    result = self.dpl.DPLSplitPageText(self.instanceID, Options)
    return result

  def StartPath(self, StartX, StartY):
    result = self.dpl.DPLStartPath(self.instanceID, StartX, StartY)
    return result

  def StoreCustomDataFromFile(self, Key, FileName, Location, Options):
    result = self.dpl.DPLStoreCustomDataFromFile(self.instanceID, Key, FileName, Location, Options)
    return result

  def StoreCustomDataFromString(self, Key, NewValue, Location, Options):
    NewValueBuffer, NewValueUsed = self.StringParm(NewValue)
    result = self.dpl.DPLStoreCustomDataFromString(self.instanceID, Key, NewValueBuffer, Location, Options)
    if NewValueUsed:
      self.dpl.DPLReleaseBuffer(self.instanceID, NewValueBuffer)
    return result

  def TestTempPath(self):
    result = self.dpl.DPLTestTempPath(self.instanceID)
    return result

  def TransformFile(self, InputFileName, Password, OutputFileName, TransformType, Options):
    result = self.dpl.DPLTransformFile(self.instanceID, InputFileName, Password, OutputFileName, TransformType, Options)
    return result

  def UnlockKey(self, LicenseKey):
    result = self.dpl.DPLUnlockKey(self.instanceID, LicenseKey)
    return result

  def Unlocked(self):
    result = self.dpl.DPLUnlocked(self.instanceID)
    return result

  def UpdateAndFlattenFormField(self, Index):
    result = self.dpl.DPLUpdateAndFlattenFormField(self.instanceID, Index)
    return result

  def UpdateAppearanceStream(self, Index):
    result = self.dpl.DPLUpdateAppearanceStream(self.instanceID, Index)
    return result

  def UpdateTrueTypeSubsettedFont(self, SubsetChars):
    result = self.dpl.DPLUpdateTrueTypeSubsettedFont(self.instanceID, SubsetChars)
    return result

  def UseKerning(self, Kern):
    result = self.dpl.DPLUseKerning(self.instanceID, Kern)
    return result

  def UseUnsafeContentStreams(self, SafetyLevel):
    result = self.dpl.DPLUseUnsafeContentStreams(self.instanceID, SafetyLevel)
    return result

