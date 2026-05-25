from kivy.core.window import Window
from kivy.logger import Logger
from kivy.metrics import dp
from kivy.utils import platform


ANDROID_PLATFORM = platform == "android"


if ANDROID_PLATFORM:
    try:
        from android.runnable import run_on_ui_thread
        from jnius import (
            PythonJavaClass,
            autoclass,
            java_method,
        )

        activity = autoclass("org.kivy.android.PythonActivity")

        AdListener = autoclass(
            "com.google.android.gms.ads.AdListener"
        )

        AdMobAdapter = autoclass(
            "com.google.ads.mediation.admob.AdMobAdapter"
        )

        AdRequest = autoclass(
            "com.google.android.gms.ads.AdRequest"
        )

        AdRequestBuilder = autoclass(
            "com.google.android.gms.ads.AdRequest$Builder"
        )

        AdSize = autoclass(
            "com.google.android.gms.ads.AdSize"
        )

        AdView = autoclass(
            "com.google.android.gms.ads.AdView"
        )

        Bundle = autoclass(
            "android.os.Bundle"
        )

        Gravity = autoclass(
            "android.view.Gravity"
        )

        InterstitialAd = autoclass(
            "com.google.android.gms.ads.InterstitialAd"
        )

        LayoutParams = autoclass(
            "android.view.ViewGroup$LayoutParams"
        )

        LinearLayout = autoclass(
            "android.widget.LinearLayout"
        )

        MobileAds = autoclass(
            "com.google.android.gms.ads.MobileAds"
        )

        RewardItem = autoclass(
            "com.google.android.gms.ads.reward.RewardItem"
        )

        RewardedVideoAd = autoclass(
            "com.google.android.gms.ads.reward.RewardedVideoAd"
        )

        RewardedVideoAdListener = autoclass(
            "com.google.android.gms.ads.reward.RewardedVideoAdListener"
        )

        View = autoclass(
            "android.view.View"
        )

        class AdMobRewardedVideoAdListener(PythonJavaClass):

            __javainterfaces__ = (
                "com.google.android.gms.ads.reward.RewardedVideoAdListener",
            )

            __javacontext__ = "app"

            def __init__(self, listener):
                super().__init__()
                self._listener = listener

            @java_method(
                "(Lcom/google/android/gms/ads/reward/RewardItem;)V"
            )
            def onRewarded(self, reward):
                Logger.info("KivMob: onRewarded() called.")

                self._listener.on_rewarded(
                    reward.getType(),
                    reward.getAmount(),
                )

            @java_method("()V")
            def onRewardedVideoAdLeftApplication(self):
                Logger.info(
                    "KivMob: "
                    "onRewardedVideoAdLeftApplication() called."
                )

                self._listener.on_rewarded_video_ad_left_application()

            @java_method("()V")
            def onRewardedVideoAdClosed(self):
                Logger.info(
                    "KivMob: onRewardedVideoAdClosed() called."
                )

                self._listener.on_rewarded_video_ad_closed()

            @java_method("(I)V")
            def onRewardedVideoAdFailedToLoad(self, errorCode):
                Logger.info(
                    "KivMob: "
                    "onRewardedVideoAdFailedToLoad() called."
                )

                self._listener.on_rewarded_video_ad_failed_to_load(
                    errorCode
                )

            @java_method("()V")
            def onRewardedVideoAdLoaded(self):
                Logger.info(
                    "KivMob: onRewardedVideoAdLoaded() called."
                )

                self._listener.on_rewarded_video_ad_loaded()

            @java_method("()V")
            def onRewardedVideoAdOpened(self):
                Logger.info(
                    "KivMob: onRewardedVideoAdOpened() called."
                )

                self._listener.on_rewarded_video_ad_opened()

            @java_method("()V")
            def onRewardedVideoStarted(self):
                Logger.info(
                    "KivMob: onRewardedVideoStarted() called."
                )

                self._listener.on_rewarded_video_ad_started()

            @java_method("()V")
            def onRewardedVideoCompleted(self):
                Logger.info(
                    "KivMob: onRewardedVideoCompleted() called."
                )

                self._listener.on_rewarded_video_ad_completed()

    except Exception as e:
        Logger.error(
            "KivMob: Cannot load AdMob classes. "
            "Check buildozer.spec."
        )

        Logger.error(f"KivMob: {e}")

else:

    class AdMobRewardedVideoAdListener:
        pass

    def run_on_ui_thread(x):
        return x


class TestIds:
    """
    Enum of test ad ids provided by AdMob.
    """

    APP = "ca-app-pub-3940256099942544~3347511713"

    BANNER = "ca-app-pub-3940256099942544/6300978111"

    INTERSTITIAL = "ca-app-pub-3940256099942544/1033173712"

    INTERSTITIAL_VIDEO = (
        "ca-app-pub-3940256099942544/8691691433"
    )

    REWARDED_VIDEO = (
        "ca-app-pub-3940256099942544/5224354917"
    )


class AdMobBridge:

    def __init__(self, appID):
        self.appID = appID

    def add_test_device(self, testID):
        pass

    def is_interstitial_loaded(self):
        return False

    def new_banner(self, unitID, top_pos=True):
        pass

    def new_interstitial(self, unitID):
        pass

    def request_banner(self, options=None):
        pass

    def request_interstitial(self, options=None):
        pass

    def show_banner(self):
        pass

    def show_interstitial(self):
        pass

    def destroy_banner(self):
        pass

    def destroy_interstitial(self):
        pass

    def hide_banner(self):
        pass

    def set_rewarded_ad_listener(self, listener):
        pass

    def load_rewarded_ad(self, unitID):
        pass

    def show_rewarded_ad(self):
        pass


class RewardedListenerInterface:
    """
    Interface for rewarded video ad callbacks.
    """

    def on_rewarded(self, reward_name, reward_amount):
        pass

    def on_rewarded_video_ad_left_application(self):
        pass

    def on_rewarded_video_ad_closed(self):
        pass

    def on_rewarded_video_ad_failed_to_load(
        self,
        error_code,
    ):
        pass

    def on_rewarded_video_ad_loaded(self):
        pass

    def on_rewarded_video_ad_opened(self):
        pass

    def on_rewarded_video_ad_started(self):
        pass

    def on_rewarded_video_ad_completed(self):
        pass


class AndroidBridge(AdMobBridge):

    @run_on_ui_thread
    def __init__(self, appID):
        super().__init__(appID)

        self._loaded = False
        self._listener = None
        self._test_devices = []

        MobileAds.initialize(
            activity.mActivity,
            appID,
        )

        self._adview = AdView(activity.mActivity)

        self._interstitial = InterstitialAd(
            activity.mActivity
        )

        self._rewarded = (
            MobileAds.getRewardedVideoAdInstance(
                activity.mActivity
            )
        )

    @run_on_ui_thread
    def add_test_device(self, testID):
        if testID not in self._test_devices:
            self._test_devices.append(testID)

    @run_on_ui_thread
    def new_banner(self, unitID, top_pos=True):
        self._adview = AdView(activity.mActivity)

        self._adview.setAdUnitId(unitID)

        self._adview.setAdSize(
            AdSize.SMART_BANNER
        )

        self._adview.setVisibility(View.GONE)

        adLayoutParams = LayoutParams(
            LayoutParams.MATCH_PARENT,
            LayoutParams.WRAP_CONTENT,
        )

        self._adview.setLayoutParams(
            adLayoutParams
        )

        layout = LinearLayout(activity.mActivity)

        if not top_pos:
            layout.setGravity(Gravity.BOTTOM)

        layout.addView(self._adview)

        layoutParams = LayoutParams(
            LayoutParams.MATCH_PARENT,
            LayoutParams.MATCH_PARENT,
        )

        layout.setLayoutParams(layoutParams)

        activity.mActivity.addContentView(
            layout,
            layoutParams,
        )

    @run_on_ui_thread
    def request_banner(self, options=None):
        self._adview.loadAd(
            self._get_builder(options).build()
        )

    @run_on_ui_thread
    def show_banner(self):
        self._adview.setVisibility(
            View.VISIBLE
        )

    @run_on_ui_thread
    def hide_banner(self):
        self._adview.setVisibility(
            View.GONE
        )

    @run_on_ui_thread
    def new_interstitial(self, unitID):
        self._interstitial.setAdUnitId(
            unitID
        )

    @run_on_ui_thread
    def request_interstitial(self, options=None):
        self._interstitial.loadAd(
            self._get_builder(options).build()
        )

    @run_on_ui_thread
    def _is_interstitial_loaded(self):
        self._loaded = (
            self._interstitial.isLoaded()
        )

    def is_interstitial_loaded(self):
        self._is_interstitial_loaded()
        return self._loaded

    @run_on_ui_thread
    def show_interstitial(self):
        if self.is_interstitial_loaded():
            self._interstitial.show()

    @run_on_ui_thread
    def set_rewarded_ad_listener(self, listener):
        self._listener = (
            AdMobRewardedVideoAdListener(
                listener
            )
        )

        self._rewarded.setRewardedVideoAdListener(
            self._listener
        )

    @run_on_ui_thread
    def load_rewarded_ad(self, unitID):
        builder = self._get_builder(None)

        self._rewarded.loadAd(
            unitID,
            builder.build(),
        )

    @run_on_ui_thread
    def show_rewarded_ad(self):
        if self._rewarded.isLoaded():
            self._rewarded.show()

    @run_on_ui_thread
    def destroy_banner(self):
        if self._adview:
            self._adview.destroy()

    @run_on_ui_thread
    def destroy_interstitial(self):
        if self._interstitial:
            self._interstitial.destroy()

    @run_on_ui_thread
    def destroy_rewarded_video_ad(self):
        if self._rewarded:
            self._rewarded.destroy()

    def _get_builder(self, options):
        options = options or {}

        builder = AdRequestBuilder()

        if "children" in options:
            builder.tagForChildDirectedTreatment(
                options["children"]
            )

        if "family" in options:
            extras = Bundle()

            extras.putBoolean(
                "is_designed_for_families",
                options["family"],
            )

            builder.addNetworkExtrasBundle(
                AdMobAdapter,
                extras,
            )

        for test_device in self._test_devices:
            builder.addTestDevice(
                test_device
            )

        return builder


class iOSBridge(AdMobBridge):
    # TODO
    pass


class KivMob:
    """
    Allows access to AdMob functionality.
    """

    def __init__(self, appID):
        Logger.info(
            "KivMob: __init__ called."
        )

        self._banner_top_pos = True

        if platform == "android":
            Logger.info(
                "KivMob: Android platform detected."
            )

            self.bridge = AndroidBridge(appID)

        elif platform == "ios":
            Logger.warning(
                "KivMob: iOS not yet supported."
            )

            self.bridge = iOSBridge(appID)

        else:
            Logger.warning(
                "KivMob: Ads will not be shown."
            )

            self.bridge = AdMobBridge(appID)

    def add_test_device(self, device):
        Logger.info(
            "KivMob: add_test_device() called."
        )

        self.bridge.add_test_device(device)

    def new_banner(self, unitID, top_pos=True):
        Logger.info(
            "KivMob: new_banner() called."
        )

        self.bridge.new_banner(
            unitID,
            top_pos,
        )

    def new_interstitial(self, unitID):
        Logger.info(
            "KivMob: new_interstitial() called."
        )

        self.bridge.new_interstitial(unitID)

    def is_interstitial_loaded(self):
        Logger.info(
            "KivMob: is_interstitial_loaded() called."
        )

        return self.bridge.is_interstitial_loaded()

    def request_banner(self, options=None):
        Logger.info(
            "KivMob: request_banner() called."
        )

        self.bridge.request_banner(options)

    def request_interstitial(self, options=None):
        Logger.info(
            "KivMob: request_interstitial() called."
        )

        self.bridge.request_interstitial(options)

    def show_banner(self):
        Logger.info(
            "KivMob: show_banner() called."
        )

        self.bridge.show_banner()

    def show_interstitial(self):
        Logger.info(
            "KivMob: show_interstitial() called."
        )

        self.bridge.show_interstitial()

    def destroy_banner(self):
        Logger.info(
            "KivMob: destroy_banner() called."
        )

        self.bridge.destroy_banner()

    def destroy_interstitial(self):
        Logger.info(
            "KivMob: destroy_interstitial() called."
        )

        self.bridge.destroy_interstitial()

    def hide_banner(self):
        Logger.info(
            "KivMob: hide_banner() called."
        )

        self.bridge.hide_banner()

    def set_rewarded_ad_listener(
        self,
        listener,
    ):
        Logger.info(
            "KivMob: set_rewarded_ad_listener() called."
        )

        self.bridge.set_rewarded_ad_listener(
            listener
        )

    def load_rewarded_ad(self, unitID):
        Logger.info(
            "KivMob: load_rewarded_ad() called."
        )

        self.bridge.load_rewarded_ad(unitID)

    def show_rewarded_ad(self):
        Logger.info(
            "KivMob: show_rewarded_ad() called."
        )

        self.bridge.show_rewarded_ad()

    def determine_banner_height(self):
        height = dp(32)

        upper_bound = dp(720)

        if Window.height > upper_bound:
            height = dp(90)

        elif dp(400) < Window.height <= upper_bound:
            height = dp(50)

        return height


if __name__ == "__main__":
    print(
        "\033[92m  _  ___       __  __       _\n"
        " | |/ (_)_   _|  \\/  | ___ | |__\n"
        " | ' /| \\ \\ / / |\\/| |/ _ \\| '_ \\\n"
        " | . \\| |\\ V /| |  | | (_) | |_) |\n"
        " |_|\\_\\_| \\_/ |_|  |_|\\___/|_.__/\n\033[0m"
    )

    print(" AdMob support for Kivy\n")

    print(" Michael Stott, 2019\n")
