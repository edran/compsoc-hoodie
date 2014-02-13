#!/usr/bin/env python
 
from __future__ import braces

class Course(object):

    def __init__(self, name):
        self.name = name
        self.cost = float("inf")

class ExamBoard(object):

    def submit(self, work):
        work_is_passing_grade = len([work]) > 0
        return work_is_passing_grade
 
 
class Society(object):
 
    def __init__(self, name):
        self.name = name
        self.members = []
 
    def add_member(self, name, matric_number):
        self.members.append((name, matric_number))

class AlmightyStallman(object):

    def impart_wisdom(self):
        print('''

                                                                                            GN UGENERAL                                                                                                
                                                                                PUBLICLICENSEVe          rsion2Ju          ne                                                                           
                                                                           1991Copyr  ightC1 9891991FreeSo     ftwareFo   un dationI                                                                    
                                                                        nc5  9Te m     plePlaceSuite330BostonMA 021111307USAEveryoneIsP                                                                 
                                                                    ermittedToCopyAndDi stributeVerbatimCopiesofTh  isLicenseDocumentbutC                                                               
                                                                 hangingItIsNotAllowedPreambleTheLicensesForMostSoftwareAreDesignedToTakeAwa                                                            
                                                               yYourfreedomToShareAndC hangeItByContrasttheGNUGeneralPublicLicenseIsIntendedTo                                                          
                                                             GuaranteeYourFreedomToShareAndChangeF   reeso  f  tw aretoMakeSureTheSoftwar eIsFr                                                         
                                                           eeForAllItsUsersT hisGeneralPublicLic  ens     eA  p       p   liesToMostOfTheFreeSof t                                                      
                                                          wareFoundationsSoftwareAndToAnyOt h  erPr  ogramW ho  se Au   t horsCommitTousingItSomeOt                                                     
                                                        herFreeSoftwareFoundationSoftw ar     e        I              s Cov er edBytheGNULibraryGen e                                                   
                                                       ralPublicLicenseInsteadYouCa  nA      p  p     l  y        I             tToyourProgramstooWh en                                                 
                                                    WeSpeakOfFreeSoftwarewe AreReferr       i  n      g             T  oFre e do  mnotpriceOurGeneralP u                                                
                                                blicLicensesAreDesignedT oMake  Su                  re                     Th  at YouhaveTheFreed omToD is                                              
                                              tributeCopiesOfFreeSoftwar eand Ch                                                 ar geF orthisServ  iceI fY                                             
                                            ouWishthatYouReceiveSou  r ceCod                                                eO    rC anG etItifYouWantItthat                                            
                                          YouCanChangeTheSoftware OrUsePi                                                       e  ce sOfItinNewFreePro grams                                           
                                         AndThatYouKnowYouCanDoTheseTh                                                              ingsToProtectYourRig  htswe                                         
                                        NeedToMak eRestrictionsTh                                                               a tForbi   danyoneToDenyYou  Thes                                       
                                        eRightsOrToAskYouToS                                                                u   r renderTh   eRigh tsTheseRestrict                                      
                                       ionsTranslateToCerta                                                                 i       nR  espo  nsibi litiesForYouIfYoud                                  
                                       istributeCopiesOfT                                                                     h      eSo ftwa  reorI fYouModifyItFor  Examplei                          
                                      fYouDistributeCopi                                                                       es O f Suc  hAProgramwh ethergratisOrF         or                        
                                     AFeeyouMustGiveTh   e                                                                      R  e  cip i entsAllTheRightsThatyouHaveY                                
                                    ouMustMakeSureTha tT                                                                         h  ey  too receiveOrCanGetThesourceCodeA                               
                                  ndYouMustShowThemThes e                                                                        Ter ms  SoT h eyKnowTh eirrightsWeProtec t                             
                               Yo  urRights WithTwoSt                                                                           eps      1 CopyrightTheS   oftwarean d 2Of                              
                              f    erYouThisLicenseW h  i                                                                        ch   G     ivesYouLegalPe  rmissionToCopyd is                          
                             t    ribut eAndorModifyTh eS o                                                                    f       twar eAlsoforEachAutho rsProtectionAnd Ou                        
                                  rsweWantToMak eC ert a         i                                                         n       th  a  t  EveryoneUnderstandsThatThereIsNoWarr  a                    
                                 nty ForThisFr  ee  soft wa                                                                     r e    I f  The SoftwareI sModifiedBySomeoneElseA                       
                                ndPassedOnwewan tItsRe        c                                                              i    pi   ent s  ToKnowThatWh atTheyHaveIsNotTheOrigina                    
                                lsothatAnyPr oblem sIntr o  d    u                                                         c      e d B yO   thersWillNotReflectOnTheOriginalau  t                      
                              horsReputationsFinal  ly an                                                                   y   F  r e e  Pr  ogramIsT hreatenedConstantlyBySoftw a  re                 
                             patentsWeWishToAvoidTheDange                                                                            rT  hatRedistributorsOfAFreeprogramWillIndivi du a                 
                            llyObt ainPatentLicens esin Eff                                                                     ectM   akin  g   TheprogramProprietaryToPreventThis weHav               
                             eMadeItClearThatAnypatentMust  B                                            eLic  ens e dForEver        yon  esFreeU   seOrNotLicensedAtAllThePreciseTe r  ms              
                            AndConditionsForCopyingdi st r                                            i   butionAndm odificatio     nFollowG NUGE NE  RALPUBLICLICENSETERMSANDCONDIT      I             
                            ONSFORCOPYINGDISTRIBUTIONAN  D                                              M ODIFICATION0ThisLice n        s  eAppliesTo  AnyProgramOrOtherWorkWhichConta  i n             
                         s  aNoticePlacedByTheC  opyright           Holde rS                          a  yingItMayBeDist  r ibutedund     e   rTheT  e  rmsOfThisGeneralPublicLicenseTh    e            
                           ProgrambelowrefersToA nySuc h        ProgramOrW                             o                         rkandAw   orkB   asedOnTheProgrammeansEi therTheProgra     m           
                          OrAnyDerivativeWorkUnderCop    yrightLawthatIsToSayaWo                                           r   k   Co  nta    inin gTheProgramOrAPortionO fIteitherVerbat               
                         i mOrWithModificationsAndorTr anslatedIntoAnotherl an                       guag eH                 ere   inaftertran  s la  tio nIsIncludedWithoutLimitationInth              
                        e TermmodificationEachLicens  eeIsAdd                 r e                   ss     edAsyouAc        tivitiesOt   her  Tha   nCopyingdistributionA ndModificationAr  e N         
                         o tcoveredByThisLicenseTheyAreOu                       tsideIt           s     ScopeTh  eActOfrunningT he  Pro      g      r a m IsNotRestrictedandTheOutputFromTh    e        
                        Pr ogramisCovere dOnlyIfItsContent  s      ConstituteA    WorkB          as ed OnTh eProgramind ependentOfHav in    gB een   Ma de ByRunningTheProgramWhetherThatIsTr           
                     u  eDependsOnWhatTheProgramDo es1 Y o uMayCop           yAndDistrib         uteVerbatimCop    iesOfThePr    ogramssou       rc e  C od eAsYouReceiveItinAnyM ediumprovi d          
                       e dThatYouconspicu ouslyAn dAppropriatel  yPublishOnEac   hCopyAn          Appro   p         r iateco   py rightNoti ce    A  nd  DisclaimerOfWarrantyKeep IntactAllTh e         
                       n oticesThatReferToThisLicenseAn dToT heAbsenc eOfA   nyWa   rran         ty  an  dGiveAnyOthe      r Rec  ip ientsOf      T    heP rogramACopyOfThis LicensealongWithTh  e      
                      P rogramYouMayChargeAFeeFo rTheP hysicalAct OfTransf      er  rin           gA Co     p      y  a    n      dyouMa yAtY        o u   rOptionOfferWarran tyProtectionInExc  h      
                      angeForAFee2YouMayModi fyYou rCopyOrCop   iesOfTheProgramOrAn yP             ortion    o fI              tthusF   o           r     min  gAWorkBasedOnTheProgramandCopyAnd  d     
                    istributeSuchModificationsO r   WorkUnder            Th     e  Ter              ms OfS    ec t ion1abovep  r      o  vi    de  dTha  tYouA lsoM eetAllOfTheseConditionsaYouMu       
                    s tCauseTheModifiedFilesToCarr  yProminen tNotic e       s    sta               tingThat  Y       ouChang e           dT          h  e Fi lesAndTheDateOfAnyChangebYouMustCa  u     
                  se AnyWorkThatYouDistributeOr Publishtha t            Inwho    leOr I         n    Part   Con                        ta             i nsOr Is DerivedFromTheProgramOrAnypartThe r     
                   eoftoBeLicensedAsAWholeAtNoC    hargeToAllT       hirdp a  rtiesU n                   de                              r         T    heTerm sOfThisLic ensecIfTheModifiedProgramN    
                 o r mallyReadsCommandsInteracti velyw henRunyouMus tCa us  e   Itw he                    nSt               a                        rtedR u n ningForSuchin teractiveUseInTheMos  tO   
                r  dinaryWaytoPrintOrDisplayAna    nnou   n ce     m     e   n  tIn cl                                  u                  d            in gAnA ppropriateCopyrightNoticeAndAnoticeTh   
               a  tThereIsNoWarrantyorElsesayin  gThat Yo        u P  r        ovi  de          a   War                          r      an             ty AndTh atUsersMayRedistributeTheProgramUnder   
                theseConditionsandTellingTheUs  erH                            ow ToVi         e wA                                                     C opyO fThisLicenseExceptionIfTheProgra mItse   
               lfIsInteractiveButdoesNotNormal l  yP                 r      in   tSuch       A  n Ann                                                     ouncementyourWorkBasedOntheProgr amIsNotRequ  
            i re  dToPrintAnAnnouncementThese  Re               qu  i    r e   m ent              sApp   l                                              y  ToT heModifiedWorkAsAWholeIfidentifiableSect 
           i  o   nsOfThatWor kAreNotDerivedFromTh   e                           Pro                gramandC                                             a nBeRea  sonablyConsideredIndependentAn dSepa 
             ra teWorksInthemselvesthenThisL ice   ns                           ea n                 dIt sTerm                                   s     do  No  tAp plyT oThosesectionsWhenYouDistributeT
        h  em AsSeparateWorksButWhenYoudistr i b u                             teT                      h    eS                                     am  eSecti o n  sAsPartOfAWholeWhichIsAWorkBasedonTh
           eP r ogramtheDi stributionOfTheWhole  M  u  s                      tBe                             On                                          T heT er  msO fthisLicensewhos ePermissionsFor
           O th erLicenseesExtendToTheentireW   h                             o  l                            ea                                        ndT husToEa chAndEveryPartRegard lessOfWhoWroteI
           t ThusitIsNotTheIntentOfThisSectionTo  C                        l ai   mR               ightsOrCo nte       s t                              y ou  rRightsToWorkWrittenEntirelyByYouRatherthe
          In tentIsToexerciseTheRightToControl  T h   e                      Di stribut          ionOfDe     ri          va                           t  iveOrcol le ctiveWorksBasedOnTheProgramInAdditi
          onmereAggregationOfAnotherWorkNotBase   d  O                  nT    heP  rogram    w ithTh        e    Pr        og                            ramo r Wi t hAWorkBasedOnTheProgramOnAVolumeOfa
         S torageOrDistributionMediumDoesNotBri ngT                       h    eO    therWorkUnde r   theSc   opeOfTh   is   Li                          cense3YouMa yCopyAndDistribute TheProgramorAWor
          kBa sedOnItunderSection2InObjectCodeOr E                             xe cu      tableF  ormUnderTheT  ermsOfSe  ct   i                on       s1 And2AboveProvidedThatYouAlsoDoOneOfTheFo llo
          wi ngaAccompanyItWithTheCompleteCorrespond                        i ngMachiner           e  adablesource Co dewhichM  us                t   Be Di stributedU nderTheTermsOfSection s1And2Above
         OnA MediumCustomarilyUsedForSoftwareIn   te                        rchangeOrbAccompa   nyItWithAWrittenOfferv  ali dFo rAt                L   ea s tThreeyear  stoGiveAnyThirdP  artyforACharge
        No M  oreThanYourcostOfPhysicallyP erform   in g             Sour ceDistributionaComplet emachinere adableCopyOfTheCorr espo           n   di    ngSourceCodetoBedistributedUnde rTheTermsOfSect
       i ons  1And2AboveOnAMediumcustomarilyUs     ed                   Fo  rSoftwareInterchang  eOrcAccompanyItWithTheIn  formationY               o    uRece ivedAsToT heOffertoDistributeCorrespondin
        g  SourceCodeThisAlternativeIsallowedOnl   yF         o    r N oncommercialDistributionAndOnlyIfYou receivedT heProgramI nObj ec           tC o  deOrExecutableFormWithSuchanOfferinA ccordWithS
        u   bsectionBAboveTheSourceCodeForAWor  kM  e      a          nsThePreferredFo rmOfTheWorkFor m aking Modific   ationsToI tFor  A       n  Ex e cuta bleWorkcompleteSourceco deMeansAllTheSource
        Co   deForAllModulesItContainsplusAny associ a         t   edIn te rfaceDefin itionFile splus Th e  ScriptsUsed T oco ntr  olC    o         mpil  ationAndInstallationOfTheExecutableHoweverasAs
           pecialExceptiontheSourceCodeDistribu te d N     e   e  dNotIncludean ythi  ngThatIsNo rmallyDistributedinEitherSourceO r Bin     ar   yf  orm  W ithTheMajorCo mpone ntscompilerkernelandSoOn
           O fTheoperatingSystemOnWhichTheExecutab            l  eRunsunlessThatCompone nt itselfAccompa nie sThe   Ex ecutab  le  IfDi  s  t r  ibu  tio nOfExecutabl eOrObjectCodeIsMadeByOfferingacce
          s   sToCopyFromADesignatedPlacethenOfferin gEq    uiv alen ta ccessToCopyTheSourceCode FromTh eSamePlac  eCou ntsA sdi  stribu  tio n    O  fThe SourceCodeev enThoughThirdPart iesAreNotcompe
          ll   edToCopyTheSourceAlongWithTheObjectC o   de   4YouMayN otCopymodifysubli cens             eo    rD   istribute  T heProgr   a   m   exceptAsExpre sslyProvi dedUnderThisLi censeAnyAttemp
         t  otherwiseToCopymodifysublicenseOrD istrib  u  t  eThe  ProgramIsvoidandWill   A      ut            oma ticall     y T e rmin  at  e Y  ou rRightsUnderThisLicenseHow everpartiesWhoHaveRecei
         v  edCopiesorRightsfromYouUnderthisLicense W il lNotHaveTheirLic  ensesTerm  i           n       a t     ed SoLongAsS uchpartie   sR e   mainInFullCompliance5YouAreNotRequiredToAcceptThisLice
          n  sesinceYouHaveNotsignedItHowevernothingEl   s  eGran ts YouPer  mission  To  Mo      d    if  yOrdis trib   uteTheProgra mO rItsDeri  vativeWorksTheseActionsArepr  ohibitedByLawIfYouDoNot
            AcceptThisLicenseThereforebymodifyin gOrD istributi ng  TheP  r   ogra morAnyWorkBase   d   OnThe P rogra my  ouIndicateY  o  ur Acc eptanceOfThisLicenseToDoSoandallItsTermsAndConditionsFo
            rCopyingdistributingOrModifyingtheProgram OrWork sBasedOn It6Ea c  hTimeY ouRedi     stribute      T h           eProgr   am  orAny WorkBasedOnTheProgramtheRecipientAutomaticallyReceivesAL
              icenseFromTheoriginalLicensorToCopydis tributeOr Modify TheP  r   o gramS ubj     e  c        t To     t heseTermsAndCond  i  tion   sYouMayNotImposeAnyFurtherrestrictionsOnTheRecipients
            GN  UGENERALPUBLICLICENSEVersion2June1991CopyrightC19891 991   Fr   e    eSoftwa          r           e Fo    un    dationIn  c 59Temp lePlaceSuite330BostonMA0211 11307USAEveryoneIsPermitt
            ed ToCopyAndDistributeVerbatimCopiesofThisLicens eD ocumentbutCh  a  ng in    g I   tI               sNo  t      Al lowedP reamble TheLicen sesForMostSoftwareAreDesignedToTakeAwayYourfreed
          o m  ToShareAndChangeItByContrasttheGNUGeneralPub licLi  censeIsIn te     n  d     e  d           ToGuaran  t     ee  YourFre   ed om ToShareAndChangeFreesoftwaretoMakeSureTheSoftwareIsFreeF
           or AllItsUsersThisGeneralPublicLicenseApplies ToMostOf TheFree     S   of     twa  re Fo  un dat  ions  So ftware  A   ndToAnyOthe rProgramWhoseAuthorsCommitTous ingItSome OtherFreeSoftware
           F  oundationSoftwareIsCoveredBytheGNULibraryGeneralP ubli c Licens e In  s te adYo uCanApplyItToyour Pr  og         ra mst ooWh en WeSpeakOfFreeSoftwareweAreReferringToFreedomnotpriceOurGen
           er alPublicLicensesAreDesignedToMakeSureThatYouhaveTheFreedom ToDis   tributeCopiesOfFreeSoftwar e a ndCharg e   ForthisServiceIfYouWishthatYouReceiveSourceCodeOrCanGetItifYouWantItthatYouC
            anChangeTheSoftwareOrUsePiecesOfItinNewFreeProgramsAndThatYouKnowYou Ca nD oTheseThingsToProtectYourRigh   tswe N eedToMakeRes tr ictionsThatForbidanyoneToDenyYouTheseRightsOrToAskYouToSur
            renderTheRightsTheseRestrictionsTranslateToCertainResponsibili tiesForYouIfYoudistributeCopiesOfTheSoftwa   reo  rIf  YouModifyItForExampleifYouDistributeCopiesOfSuchAProgramwhethergratisO
          r F orAFeeyouMustGiveTheRecipientsAllTheRightsThatyouHaveYouMustMakeSureT hatTheytooreceiveOrCanGetThe sourceCodeAnd YouMustShowThemTheseTermsSoTheyKnowTheirrightsWeProtectYourRightsWithTwoS
          t eps1CopyrightTheSoftwareand2OfferYouThisLicen seWhichGivesYouLegalPermissionToCopydistributeA   n  dorModifyTheSoftwareAlsoforEachAuthorsProtectionAndOursweWantToMakeCertainthatEveryoneUnd
          ers tandsThatThereIsNoWarrantyForThisFreesoftw areIfTheSoft wareIsModif iedBySomeoneElseAndPassed O  n wewantItsRecipientsToKnowThatWhatTheyHaveIsNotTheOriginalsothatAnyProblemsIntroducedByO
          t   hersWillNotReflectOnTheOriginalauthorsReputationsFinallyanyFreeProgramIsThreatenedCo  nst antlyByS oft warepatentsWeWishT oAvoidTheDangerThatRedistributorsOfAFreeprogramWillIndividuallyO
            btainPatentLicensesinEffectMakingTheprogramProprietaryToPreventThisweHaveMadeItClearTh atAnyp atentMustBeLicensedForEveryonesFreeUseOrNotLicensedAtAllThePreciseTermsAndConditionsForCopying
             distributionAndmodificationFollowGNUGENERALPUBLICLICENSETER MSANDCONDITIONS FORCOPYINGDISTR  I BUTIONANDMODIFICATION0ThisLicenseAppliesToAnyProgramOrOtherWorkWhichContainsaNoticePlacedByT
          h  eCopyrightHolderSayingItMayBeDistributedunderTheTermsOfThisGeneralPublic LicenseThePro grambelowrefersT oAnySuchProgramOrWorkandAworkBasedOnTheProgrammeansEitherTheProgramOrAnyDerivativeW
          o  rkUnderCopyrightLawthatIsToSayaWorkContainingTheProgramOrAPor tionOfIteitherVe rbatimOrWithModifi cationsAndorTranslatedIntoAnotherlanguageHereinaftertranslationIsIncludedWithoutLimitatio
          n  I ntheTe rmmodificationEachLicenseeIsAddressedAsyouActiv itiesOthe rThan Copyingdistributi onAndModificationAreNotcoveredByThisLicenseTheyAreOutsideItsScopeTheActOfrunningTheProgramIsNotR
          e  strictedandTheOutputFromTheProgramisCoveredOnlyIfItsContentsConstitute AW orkB asedO nThePr ogramindependentOfHavingBeenMadeByRunningTheProgramWhetherThatIsTrueDependsOnWhatTheProgramDoes
             1Y ouMayCopyAndDistributeVerbatimCopie  sOfTheProgramssourceCode AsYouR e  ceiveItinAnyMe d iumpro videdThatYouconspicuouslyAndAppropriatelyPublishOnEachCopyAnAppropriatecopyrightNoticeAn
              dDisclaimerOfWarrantyKeepIntactAllThenoticesThatReferToThisLicense AndToT  heAbsenceOfAn yW arran tyandGiveAnyOtherRecipientsOfTheProgramACopyOfThisLicensealongWithTheProgramYouMayCharge
          A   FeeForThePhysicalActOfTransferringACopyandyouMayAtYourOptionOfferWarrantyPr otectionI nExc hangeForAFee2YouMayModifyYourCopyOrCopiesOfTheProgramOrAnyP ortionofItthusFormingAWorkBasedOnTh
             e ProgramandCopyAnddistributeSuchModificationsOrWorkUn derTheTermsOfS ection 1a boveprovidedT hatYouAlsoMeetAllOfTheseConditionsaYouMustC auseTheModifiedFilesToCarryProminentNoticesstatin
            g  ThatYouChangedTheFilesAndTheDateOfAnyChangebYouMustCauseAnyWorkThatY  ouDistributeOrPu blis hthatIn whol eOrInPartContainsOrIsDerivedFromTheProgramOrAnypartThereoftoBeLicensedAsAWholeAt
                NoChargeToAllThirdpartiesUnderTheTermsOfThisLicensecIfTheModifiedProgramN ormallyReadsComma ndsInteractivelywhenRunyouMustCauseItwhenStartedRunningForSuchinteractiveUseInTheMostOrdinar
             y  WaytoPrintOrDisplayAnannouncementIncludingAnAppro priateCopyrightNoticeAndAnoticeThatThereI sNoWar rantyo rElsesayingThatYouProvideaWarrantyAndThatUsersMayRedistributeTheProgram Undert
              heseConditionsandTellingTheUserHowToViewACopy O fTh isLicenseExceptionIfTh eProgramItselfI sInteractiveButdoesNotNormallyP rintSuchAnAnnouncementyourWorkBasedOntheProgramIsNotRequiredToP
               rintAnAnnouncementTheseRequirementsApplyTo TheModifiedWorkAsAWhole IfidentifiableSec ti ons OfThatWorkAreNotDerivedFromTheProgramandCanBeReasonablyConsideredIndependentAndSeparateWorksI
            n   themselvesthenThisLicenseandItsTermsdoNotApplyToThosesectionsWhenYouDis tributeThemAsSeparateWorksButWhenYoudistributeTheSameSectionsAsPartOfAWholeWhichIsAWorkBasedonTheProgramtheDistr
                ibutionOfTheWholeMustBeOnTheTermsOfthisLicensewhosePermissionsForOtherLicenseesExtendToTheentireWholeandThusToEachAndEveryPartRegardlessOfW hoWroteItThusi tIsNotTheIntentOfThisSectionT
                  oClaimRightsOrContestyourRightsToWorkWrittenEntirelyByYouRathertheIntentIsToe xerciseTheRightToControlTh eDistributionOfDerivativeOrcollectiveWorksBasedOnTheProgramInAdditionmereAggr
                     egationOfAnotherWorkNotBasedOnTheProgramwithTheProgramorWithAW orkBasedOnTheProgramOnAVolumeOfaStorageOrDistributionMediumDoesNotBringTheOtherWorkUndertheScopeOfThisLice  nse3YouM
                  a  yC opyAndDistributeTheProgramorAWorkBasedOnItunderSection2InObjectCodeOrExecutableFormUnderTheTermsOfSections1And2AboveProvid edThatYouAlsoDoOneOfTheFollowingaAccompany ItWithTheC
                      ompleteCorrespondingMachinereadablesourceCodewhichMustBeDistributedUnderTheTermsOfSections1And2AboveOn AMediu mCustomarilyUse dForSoftwar eInterchangeOrbAccompanyItWithAWrittenOf
                      f e rvalidForAtLeastThreeyearstoGiveAnyThirdPartyforAChargeNoMoreThanYourcostOfPhysicallyPerformingSourceDistributionaComplete machinereadableCopyOfTheCorrespondingSourceCodetoBe
                          distributedUnderTheTermsOfS ections1And2AboveOnAMediumcustomarilyUsed ForSoftwareInterchangeOr cAccompanyItWithTheInformationYouReceivedAsToTheOffertoDistributeCorrespondingS
                          ourceCodeThisAlternativeIsallowedOnlyForNoncom mercialDist ributionAndOnlyIfYoure ceivedTheProgramInObjectCodeOrExecutableFormWithSuchanOfferinAccordWithSubsectionBAboveTheSo
                         u rceCodeForAWorkMeansThePreferredFormOfTheWorkFormakingModificationsToItForAnExecutableWorkcompleteSourceco deMeansAllTheSourceCodeForAllModulesItContainsplusAnyassociatedInt
                          e rfaceDefinitionFilesplusTheScriptsUsedTocontrolCompilationAndInstallationOfTheExecutableHoweverasAspecialExceptiontheSourceCodeDistributedNeedNotIncludeanythingThatIsNormal
                           lyDistributedinEitherSourceOrBinaryformWithTheMajorComponentscompilerkernelandSoOnOfTheoperatingSystemOnWhichTheExecutableRunsunlessThatComponentitselfAccompaniesTheExecutab
                          leIfDistributionOfExecutableOrObjectCodeIsMadeByOfferin gaccessToCopyFromADesignatedPlacethenOfferingEquivalentaccessToCopyTheSourceCodeFromTheSamePlaceCountsAsdistributionOf
                         TheSourceCodeevenThoughThirdPartiesAreNotcompelledToC opyTheSourceAlongWithTheObjectCode4YouMayNotCopymodifysublicenseorDistributeTheProgramexceptAsExpresslyProvidedUnderThisL
                      icenseAnyAttemptotherwiseToCopymodifysublicenseOrDistributeTheProgramIsvoidandWillAutomaticallyTerminateYourRightsUnderThisLicenseHoweverpartiesWhoHaveReceivedCopiesorRightsfromY
                    ouUnderthisLicenseWillNotHaveTheirLicensesTerminatedSoLongAsSuchpartiesRemainInFullCompliance5YouAreNotRequiredToAcceptThisLicensesinceYouHaveNotsignedItHowevernothingElseGrantsYou
                  PermissionToModifyOrdistributeTheProgramOrItsDerivativeWorksTheseActionsAreprohibitedByLawIfYouDoNotAcceptThisLicenseTh erefo    rebymodifyingOrDistributingTheProgramorAnyWorkBasedOn
                 TheProgramyouIndicateYourAcceptanceOfThisLicenseToDoSoandallItsTermsAndConditionsForCopyingdis tributingOr ModifyingtheProg ramO rWorksBasedOnIt6EachTimeYouRedistributeTheProgramorAny
              WorkBasedOnTheProgramtheRecipientAutomaticallyReceivesALicenseFromTheoriginalLicensorToCopydistributeOrModifyTheProgramS ubjectTothese TermsAndConditionsYouMayNotImposeAnyFurtherrestrict
            ionsOnTheRecipientsExerciseOfTheRightsGrantedHereinYouAreNotResponsibleForEnforcingComplianceByThirdPart iesTot  hisLicense7Ifa s   AConsequenceOfACourtJudgmentOrAllegationOfPatentinfringe        ''')


TheSavior = AlmightyStallman()
 
class Student(object):
 
    def __init__(self, name, matric_number, course):
        self.money = 0
    def __init__(self, name, matric_number):
        TheSavior.impart_wisdom()
        self.at_university = True
        self.member_societies = {}
        self.graduated = False
        self.name = name
        self.matric_number = matric_number
        self.course = course
        

    def fucks_given(self):
        yield None
 
    def join_society(self, society):
        self.member_societies[society.name] = society
        society.add_member(self.name, self.matric_number)
 
    def have_fun(self):
        #TODO: Implement fun
        pass
 
    def do_work(self):
        #TODO: Implement
        try:
            1/0
        except:
            self.have_fun()
 
    def graduate(self):
        self.graduated = True
        self.member_societies = {}

    def __init__(self):
        self.cost = float("inf")
    
    def grad_ceremony(self):
        if self.money > course.cost:
            print "Many beers!"
            return 1
 
 
def main():
    comp_soc = Society('comp_soc')
 
    student = Student('Jacob Essex', 's104340', "AI&CS")
    student.join_society(comp_soc)
    
    board_of_examiners = ExamBoard()
 
    while not student.graduated and 'comp_soc' in student.member_societies:
        success = board_of_examiners.submit(student.do_work() for fucks in student.fucks_given())
        if not success:
            student.have_fun()
    
    if not student.drunk and student.graduated:
        student.grad_ceremony()
 
if __name__ == '__main__':
    main()
    
